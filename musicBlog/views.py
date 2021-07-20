from django.db.models.query_utils import Q  # Q 객체를 이용하여 검색 기능 구현
from django.shortcuts import render, redirect, get_object_or_404  #404는 서버가 요청한 페이지를 찾을 수 없다.
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm

def home(request):
    blog_list = Blog.objects.all()   
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')  
    blogs= paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id): 
    blog = get_object_or_404(Blog, pk = id) 
    return render(request, 'detail.html', {'blog':blog})

def new(request):  
    if request.method == 'POST':
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)  
            new_post.save()
            return redirect('home')
    else:
        post_form = BlogForm()
        return render(request, 'new.html', {'post_form':post_form})

def edit(request, id): 
    edit_post = get_object_or_404(Blog, pk=id)
    if request.method == 'GET':
        post_form = BlogForm(instance = edit_post)
        return render(request, 'edit.html', {'post_form':post_form})
    else:
        post_form = BlogForm(request.POST, request.FILES, instance = edit_post)
        if post_form.is_valid():
            edit_post = post_form.save(commit=False)  
            edit_post.save()
            return redirect('detail', edit_post.id)      

def delete(request, id):   
    delete_post = Blog.objects.get(id=id)
    delete_post.delete()
    return redirect('home') 

def search(request):
    blog_list = Blog.objects.all()   
    search_key = request.POST.get('search_key', '') # 검색어 가져오기
    search_type = request.POST.get('search_type', '') # 검색 타입 가져오기

    # 만약 검색어가 존재하면
    if search_key:  
        if search_type == 'title':
            blog_list = blog_list.filter(title__icontains=search_key)   # 제목에서 해당 검색어를 포함한 queryset 가져오기
        elif search_type == 'singer':
            blog_list = blog_list.filter(singer__icontains=search_key)  # 가수에서 해당 검색어를 포함한 queryset 가져오기
        elif search_type == 'genre':
            blog_list = blog_list.filter(genre__icontains=search_key)   # 장르에서 해당 검색어를 포함한 queryset 가져오기
        elif search_type == 'lyrics':
            blog_list = blog_list.filter(lyrics__icontains=search_key)  # 가사에서 해당 검색어를 포함한 queryset 가져오기
        elif search_type == 'title_lyrics':
            blog_list = blog_list.filter(Q (title__icontains=search_key) | Q (lyrics__icontains=search_key))   # 제목, 가사에서 해당 검색어를 포함한 queryset 가져오기
        return render(request, 'search.html', {'blogs':blog_list, 'search_key':search_key, 'search_type':search_type})
    else:
        return render(request, 'search.html')

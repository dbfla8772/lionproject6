from django import forms
from .models import Blog

class BlogForm(forms.ModelForm): # 장고에서 지원해주는 forms를 상솓받음
    class Meta: 
        model = Blog 
        fields = ['title', 'singer', 'genre', 'composer', 'rel_date', 'lyrics', 'image']
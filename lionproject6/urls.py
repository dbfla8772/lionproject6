from django.contrib import admin
from django.urls import path, include
from musicBlog import views
from musicBlog.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('musicBlog/', include('musicBlog.urls')), 
    path('accounts/', include('allauth.urls')), # 이미 url이 존재(가져다 쓰기만 하면 됨)  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
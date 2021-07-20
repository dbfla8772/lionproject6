from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=200)    # 노래 제목
    singer = models.CharField(max_length=100)   # 가수 이름
    genre = models.CharField(max_length=50)     # 노래 장르
    composer = models.CharField(max_length=30)  # 노래 작곡가
    rel_date = models.CharField(max_length=10)  # 발매 날짜 (년도, 월, 일 합해서 10자리 ex. 2021/01/01)
    lyrics = models.TextField()                # 노래 가사
    image = models.ImageField(upload_to='musicBlog/', blank=False, null=False)  # 노래 커버 사진
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(120,100)], format="JPEG", options={'quality':60})  # 썸네일

    def __str__(self):
        return self.title

    def summary(self):
        return self.lyrics[:100]  



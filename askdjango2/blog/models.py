
import re
from django.forms import ValidationError
from django.db import models
from django.utils import timezone
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    author = models.CharField(max_length =20)
    title = models.CharField(max_length=100,verbose_name ='제목',
        help_text='포스팅 제목을 최대 4자이상쓰시오') #길이 제한이 있는문자열
    content = models.TextField(verbose_name='내용') #길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True)#처음만들어질떄마다 저장
    updated_at = models.DateTimeField(auto_now = True)#갱신할때마다 저장
    
    status = models.CharField(max_length=1,choices = STATUS_CHOICES)
    tags = models.CharField(max_length=100,blank = True)
    lmglat = models.CharField(max_length=50,blank = True,
        validators= [lnglat_validator],  #유효성검사 lmglat라인에 원하는조건을 써서 만들어진거ㅣㅇㅁ
        help_text = '위도/경도 포맷으로 바꿈')
    
    class Meta:
        ordering = ['-id']


def __str(self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length =20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




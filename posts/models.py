
import datetime
from pyexpat import model
from typing import Text
from django.db import models

from django.conf import settings
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/%y/%m/%d')
    caption=models.TextField(blank=True)
    title=models.CharField(max_length=200)
    slug =models.SlugField(max_length=200,blank=True)
    created=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='post_liked',blank=True)
    
    def __str__(self) :
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)
        
        
        
class comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment')
    body=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now=True)
    posted_by=models.CharField(max_length=200)
    
    class Meta:
        ordering=('created',)
    def __str__(self):
        return self.body
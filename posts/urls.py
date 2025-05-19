from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('create/',views.post_create,name='post_create'),
    path('feed/<str:pk>',views.feed,name='feed_post'),
    path('like/',views.like_post,name='liked_post'),
    
] 
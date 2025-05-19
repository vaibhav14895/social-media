from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm,Commentform
from .models import Post
from django.shortcuts import get_object_or_404
from app.models import Profile
from django.contrib.auth.models import User
@login_required
def post_create(request):
    if request.method =="POST":
        form=PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_item=form.save(commit=False)
            new_item.user=request.user
            new_item.save()
        else:
            print(form.errors)
    else:
        
        form=PostCreateForm(data=request.GET)
    return render (request,"posts/post_create.html",{'form':form})

def feed (request,pk):
    user = get_object_or_404(User, username=pk)
    posts = Post.objects.filter(user=user)
    profile = get_object_or_404(Profile, user=user)
    logged_user=request.user
    if request.method=="POST":
        form =Commentform(data=request.POST)
        new_comment =form.save(commit=False)
        post_id=request.POST.get('post_id')
        post=get_object_or_404(Post,id=post_id)
        new_comment.post=post
        new_comment.save()
    else:
        form=Commentform()
    return render(request,"posts/feed.html",{"posts":posts,"logged_user":logged_user,"form":form,"profile":profile})


def like_post(request):
    post_id=request.POST.get('post_id')
    post =get_object_or_404(Post,id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed_post')
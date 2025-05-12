
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditForm,ProfileEditForm
from posts.models import Post
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
@login_required
def edit(request):
    if request.method =="POST":
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)
    return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})      


def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])  
            if user is not None:
                login(request,user)
                return redirect('feed_post')
            else:
                return HttpResponse("invalid credentials")
    else:    
        form=LoginForm()
    return render(request,"users/login.html",{'form':form})

def logout_page(request):
    logout(request)
    return render(request,"users/logout.html")

@login_required
def index(request):
    current_user=request.user
    posts=Post.objects.filter(user=current_user)
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,"users/index.html",{'posts':posts,'profile':profile})

@csrf_exempt
def register(request):
    if request.method=="POST":
       user_form =UserRegistrationForm(request.POST)
       if user_form.is_valid():
           new_user=user_form.save(commit=False)
           new_user.set_password(user_form.cleaned_data['password'])
           new_user.save()
           Profile.objects.create(user=new_user)
           return JsonResponse("success")
    else:
        user_form=UserRegistrationForm()
    return render(request,'users/register.html',{'user_form':user_form} )

from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer

@api_view(['POST'])
def post(request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

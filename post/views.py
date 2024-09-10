from django.shortcuts import render, redirect
from . forms import MakePost, CustomUserCreationForm
from . models import Post
from django.contrib.auth.decorators import login_required


def index(request):
    post=Post.objects.all()
    return render(request,"index.html",{"post":post})
@login_required
def post(request):
    form=MakePost()
    if request.method=='POST':
        form=MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=MakePost()
            return redirect("home")
    return render(request,"post.html",{"form":form})
def details(request,id):
    post=Post.objects.get(id=id)
    return render(request,"details.html",{"post":post})
def delete(request,id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        post.delete()
        return redirect("home")
def edit(request,id):
    post=Post.objects.get(id=id)
    form=MakePost(instance=post)
    if request.method=='POST':
        form=MakePost(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"edit.html", {"form":form})
def register(request):
    form=CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request,"register.html",{"form":form})
def logout(request):
    logout(request)
    return redirect("login")
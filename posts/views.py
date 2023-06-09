from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html',{'post':post})

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        post = Post.objects.create(title=title, body=body)
        post.save()
        return redirect("/")
    else:
        return render(request,'add.html')
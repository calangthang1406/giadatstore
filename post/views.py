from email.mime import image
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def list(request):  #get posts in /post
    data = {'Posts': Post.objects.all().order_by("-date")}  #get posts in order from new to old (from old to new use "date")
    return render(request, 'blog/post.html', data)

def posts(request, id):  #show posts in /post 
    posts = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'posts': posts})
    

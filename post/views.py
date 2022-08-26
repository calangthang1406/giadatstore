from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def list(request):
    data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'blog/post.html', data)

def posts(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'posts': posts})
    

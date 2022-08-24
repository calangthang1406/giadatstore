from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def shop(request):
    return render(request, 'pages/shop.html')

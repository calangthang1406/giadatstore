
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    return render(request, 'pages/cart.html')
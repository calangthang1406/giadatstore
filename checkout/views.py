from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def checkout(request):
    return render(request, 'pages/checkout.html')

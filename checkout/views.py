from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse

def checkout(request):
    return render(request, 'pages/checkout.html')

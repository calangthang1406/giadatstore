from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout')
]

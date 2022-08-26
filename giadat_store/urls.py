"""giadat_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
import os
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gaugau/', admin.site.urls),
    path('', include('home_store.urls')),
    path('shop/', include('shop.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('about/', include('about.urls')),
    path('cart/', include('st_cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('post/', include('post.urls')),
    path('product/', include('product.urls')),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #load image


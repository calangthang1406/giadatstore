from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.list, name='post'),
    path('<int:id>/', views.posts, name='posts')
]

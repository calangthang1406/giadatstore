from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image =  models.ImageField(
        upload_to="",
    )
    price = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    

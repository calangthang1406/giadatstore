from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField()
    price = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

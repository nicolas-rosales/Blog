
from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField



 


class Post(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    content = RichTextField()
    publish_date = models.DateTimeField()
    # autor = admin()

    
    def __str__(self):
        return f"Titulo: {self.title} // Autor:"
class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.post    
    
class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.post   
    
    


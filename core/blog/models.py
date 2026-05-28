
from django.db import models

from accounts.models import Profile


class Post(models.Model):
    """ | class to define (post) in blog app | """
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=256)
    image = models.ImageField()
    content = models.TextField(max_length=256)
    status = models.BooleanField(default=False)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    
    
class Category(models.Model):
    """ | class to define (category) in blog app | """
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

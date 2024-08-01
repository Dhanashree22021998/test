from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):


    Choices = [
        ('Other','Other'),
        ('Science','Science'),
        ('Politics','Politics'),
        ('News','News')
    ]

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 25)
    body = models.CharField(max_length = 35)
    created_at = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    category = models.CharField(max_length = 65,choices = Choices)
    pic = models.ImageField(upload_to='blog/img',null = True,blank = True)


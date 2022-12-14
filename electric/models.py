from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Electric(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    usage=models.TextField(blank=True)
    power=models.DateTimeField(auto_now_add=True)
    voltage=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Electronics(models.Model):
    
    title=models.CharField(max_length=255)
    usage=models.TextField(blank=True)
    OS=models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
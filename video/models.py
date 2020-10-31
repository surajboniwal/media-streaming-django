from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=256)
    url = models.FileField(upload_to='videos')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    upload_date = models.DateField(auto_now_add=True)
    thumbnail = models.FileField(upload_to='thumbnail', default='default.jpg')
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
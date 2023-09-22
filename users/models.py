from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user (models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE) 

class profile (models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.users.username} profile'

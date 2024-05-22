from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=2000)
    imagen = models.ImageField(upload_to='menu/images/')
    
    def __str__(self):
        return self.title


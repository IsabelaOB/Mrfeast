from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=2000)
    imagen = models.ImageField(upload_to='menu/images/')
    
    def __str__(self):
        return self.title

class Review(models.Model): 
    text = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True)  # the current datetime will be automatically filled in
    user = models.ForeignKey(User,on_delete=models.CASCADE) # a user can create multiple reviews
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE) 
    favorito = models.BooleanField() 
    calificacion = models.IntegerField(default = 1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    def __str__(self): 
        return self.text
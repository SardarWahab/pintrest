from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile/',blank=True, null=True)
    DOB = models.DateField()
    
    def __str__(self):
        return self.username 

class Pin(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=True)
    pic = models.ImageField(upload_to='pin/',blank=False)
    savers = models.ManyToManyField(CustomUser,blank=True,related_name='saved')
    
    def __str__(self) :
        return f'Pin from {self.author} with title: {self.title}'
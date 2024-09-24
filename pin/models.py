from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pin(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=True)
    pic = models.ImageField(upload_to='pin/',blank=False)
    savers = models.ManyToManyField(User,blank=True,related_name='saved')
    def __str__(self) :
        return f'Pin from {self.author} with title: {self.title}'
from django.shortcuts import render
from django.contrib import messages
from pin.models import Pin
def home(request):
    pins = Pin.objects.all()
    context = {
        'pins':pins
    }
    return render(request,'home.html',context)
def profile(request):
    
    return render(request,'profile.html')
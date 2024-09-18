from django.shortcuts import render
def home(request):
    
    return render(request,'home.html')
def create(request):
    
    return render(request,'create.html')
def profile(request):
    
    return render(request,'profile.html')
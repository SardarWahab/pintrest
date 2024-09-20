from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from .models import Pin
# Create your views here.
def handle_login(request):
    if request.method == 'POST':
        # print('i got form data')
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = authenticate(request, username=username,password=password)
        if new_user:
            login(request,new_user)
        else:
            messages.info(request,"You have not this account, Please singup for login")

    return redirect('home')


def handle_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        exesting_username = User.objects.filter(username=username).first()
        if exesting_username:
            messages.info(request,'username already exist')
            return redirect('home')
    
        exesting_email = User.objects.filter(email=email).first()
        if exesting_email:
            messages.info(request,'Email already exist')
            return redirect('home')
        # print("i got submitted data",username,email,password)
        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
    
    return redirect('home')


def create_pin(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        pic = request.FILES.get('image')
        author = request.user
         
        new_pin = Pin(author=author,title=title, description =desc ,pic=pic)
        new_pin.save()
        messages.success(request,'your pin succesfully uploaded...')
    return render(request,'create.html')


def handle_logout(request):
    logout(request)
    messages.info(request,'You are logged out successfully')
    return redirect('home')

def single_pin(request,id):
    return render(request,'pin_page.html')
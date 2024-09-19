from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate
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
        print('no form submitted')

    return redirect('home')


def handle_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        exesting_username = User.objects.filter(username=username).first()
        if exesting_username:
            return HttpResponse('username already exist')
        exesting_email = User.objects.filter(email=email).first()
        if exesting_email:
            return HttpResponse('Email already exist')
        # print("i got submitted data",username,email,password)
        new_user = User.objects.create(username=username,email=email,password=password)
        new_user.save()
    
    return redirect('home')
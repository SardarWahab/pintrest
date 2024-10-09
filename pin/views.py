from django.shortcuts import render,redirect,HttpResponse
# from django.contrib.auth.models import User
from .models import CustomUser as User 
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
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
            messages.error(request,"You have not this account, Please singup for login")

    return redirect('home')


def handle_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        exesting_username = User.objects.filter(username=username).first()
        if exesting_username:
            messages.warning(request,'username already exist')
            return redirect('home')
    
        exesting_email = User.objects.filter(email=email).first()
        if exesting_email:
            messages.warning(request,'Email already exist')
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
    target_pin = Pin.objects.get(id=id)
    context ={
        'pin':target_pin
    }
    return render(request,'pin_page.html',context)


def my_profile(request):
    # all_pins = Pin.objects.all()
    my_pins = Pin.objects.filter(author = request.user)
    context = {
        'my_pins': my_pins
    }
    return render(request,'profile.html',context)


def delete_pin(request,id):
    target_pin = Pin.objects.get(id=id)
    if target_pin.author == request.user:
        target_pin.delete()
        messages.success(request,"your pin delete successfully")
        return redirect('home')
    


def update_pin(request,id):
    target_pin = Pin.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        target_pin.title = title
        target_pin.description = description
        target_pin.save()
        messages.success(request,"your pin Update successfully")
    context = {
        'pin':target_pin
    }
    

    return render(request,'updatePin.html',context)

@login_required
def save_pin(request,id):
    target_pin = Pin.objects.filter(id=id).first()
    if target_pin:
        target_pin.savers.add(request.user)
        target_pin.save()
        messages.success(request,"The Pin has been saved")
    else:
        messages.error(request,"Pin not found")
    return redirect('home')


def unsave_pin(request, id):
    target_pin = Pin.objects.filter(id=id).first()
    if target_pin:
        if request.user in target_pin.savers.all():
            target_pin.savers.remove(request.user)
            target_pin.save()
            messages.warning(request,"Pin Unsaved")
        else:
            messages.error(request,"You haven't saved this Pin")
    else:
            messages.error(request,"Pin not found")
    return redirect('home')
 
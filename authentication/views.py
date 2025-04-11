from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def authlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, 'invalid email or password!')
            

    return render(request, 'auth/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('login')

def authregistration(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            print('yuck')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists!')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('profile')
        
        else:
            messages.error(request, 'Passwords do not match!')



    return render(request, 'auth/registration.html') 


def authreset(request):
    return render(request, 'auth/reset.html')
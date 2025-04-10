from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'auth/login.html')


def registration(request):
    return render(request, 'auth/registration.html')


def reset(request):
    return render(request, 'auth/reset.html')
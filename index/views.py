from django.shortcuts import render
from .models import About, Slider, client

# Create your views here.

def home(request):
    aboutdata = About.objects.all()[0]
    sliderdata = Slider.objects.all()
    clientdata = client.objects.all
    context = {
        'about' : aboutdata,
        'slider': sliderdata,
        'client': clientdata,
    }
    return render(request,"index.html", context)


def about(request):
    return render(request, "about.html")


def blog(request):    
    return render(request, "blog.html")


def price(request):    
    return render(request, "price.html")


def service(request):    
    return render(request, "service.html")
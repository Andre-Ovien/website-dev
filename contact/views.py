from django.shortcuts import render
from .models import ContactList

# Create your views here.

def contact(request):
    contactdata = ContactList.objects.all()[0]
    contexts = {
        'contacts': contactdata
    }
    return render(request, "contact.html", contexts)
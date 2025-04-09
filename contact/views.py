from django.shortcuts import render
from .models import ContactList
from .models import ContactForm

# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactformdata = ContactForm(name=name,email=email,subject=subject,message=message)
        contactformdata.save()

    contactdata = ContactList.objects.all()[0]
    contexts = {
        'contacts': contactdata
    }
    return render(request, "contact.html", contexts)
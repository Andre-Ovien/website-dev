from django.contrib import admin
from .models import ContactList
from .models import ContactForm

# Register your models here.
admin.site.register(ContactList)
admin.site.register(ContactForm)
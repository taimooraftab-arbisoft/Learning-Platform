from django.shortcuts import render
from myApp.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('message')
        contact = Contact(name= name, email= email, description= desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

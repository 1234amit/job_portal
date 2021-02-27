from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'job/index.html', context={})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, number=number, desc=desc)
        ins.save()
    return render(request, 'job/contact.html', context={})

def admin_login(request):
    return render(request, 'job/admin_login.html',context={})

def recruiter_login(request):
    return render(request, 'job/recruiter_login.html', context={})
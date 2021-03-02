from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .models import Contact
from App_Login.models import UserProfile
from django.contrib.auth.models import User
from Recruiters_Login.models import Recruiters
from django.contrib.auth.decorators import login_required
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('job:admin_home')
            messages.info(request, 'Admin Login Successfully')
        else:
            messages.info(request, 'username and password are incorrect')
    context = {}
    return render(request, 'job/admin_login.html',context)

@login_required
def admin_home(request):
    return render(request, 'job/admin_home.html')


def admin_logout(request):
    logout(request)
    return redirect('job:admin_login')

@login_required
def view_users(request):
    data = UserProfile.objects.all()
    context = {'data':data}
    return render(request, 'job/view_users.html', context)


@login_required
def delete_user(request, pk):
    users = UserProfile.objects.get(id=pk)
    users.delete()
    return redirect('job:view_users')

@login_required
def recruiter_pending(request):
    data = Recruiters.objects.filter(status='pending')
    context = {'data':data}
    return render(request, 'job/recruiter_pending.html', context)

@login_required
def change_status(request,pk):
    error = ""
    recruiters = Recruiters.objects.get(id=pk)
    if request.method == 'POST':
        s = request.POST['status']
        recruiters.status = s
        try:
            recruiters.save()
            error = "no"
        except:
            error = "yes"
    context = {'recruiters':recruiters, 'error':error}
    return render(request, 'job/change_status.html', context)

@login_required
def recruiter_accepted(request):
    data = Recruiters.objects.filter(status='Accept')
    context = {'data':data}
    return render(request, 'job/recruiter_accepted.html', context)

@login_required
def recuiter_rejected(request):
    data = Recruiters.objects.filter(status='Reject')
    context = {'data':data}
    return render(request, 'job/recruiter_rejected.html', context)

@login_required
def recuiter_all(request):
    data = Recruiters.objects.all()
    context = {'data':data}
    return render(request, 'job/recruiter_all.html', context)

@login_required
def delete_recruiter(request,pk):
    recruiter = Recruiters.objects.get(id=pk)
    recruiter.delete()
    return redirect('job:recuiter_all')

@login_required
def admin_changePass(request):
    error =""
    if request.method == 'POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c == n:
            u = User.objects.get(id=request.user.id)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
    context = {'error':error}
    return render(request, 'job/admin_changePass.html', context)


def recruiter_login(request):
    return render(request, 'job/recruiter_login.html', context={})
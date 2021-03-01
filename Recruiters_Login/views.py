from django.shortcuts import render,HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Recruiters_Login.models import Recruiters
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        p = request.POST['pwd']
        e = request.POST['email']
        i = request.FILES['image']
        con = request.POST['contact']
        gen = request.POST['gender']
        com = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiters.objects.create(user=user, mobile=con, image=i, gender=gen, company=com, Type="recruiter", status="pending" )
            error="no"

        except:
            error="yes"

    d = {'error':error}
    return render(request, 'Recruiters_Login/sign_up.html', d)


def recruiter_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(request, username=u, password=p)
        if user:
            try:
                user1 = Recruiters.objects.get(user=user)
                if user1.Type == "recruiter" and user1.status != "pending":
                    login(request,user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error':error}
    return render(request, 'Recruiters_Login/recruiter_login.html',d)

@login_required
def recruiter_home(request):
    return render(request, 'Recruiters_Login/recruiter_home.html')

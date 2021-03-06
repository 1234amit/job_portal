from django.shortcuts import render,HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Recruiters_Login.models import Recruiters, Job
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from datetime import date
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
    totalRecruiters = Recruiters.objects.count()
    totalJobs = Job.objects.count()
    context = {'totalJobs':totalJobs,'totalRecruiters':totalRecruiters}
    return render(request, 'Recruiters_Login/recruiter_home.html', context)


@login_required
def recruiter_logout(request):
    logout(request)
    return redirect('Recruiters_Login:recruiter_login')

@login_required
def requiterChangePass(request):
    error =""
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    context = {'error':error}
    return render(request, 'Recruiters_Login/recuiterchangepass.html', context)

@login_required
def add_job(request):
    error = ""
    if request.method == 'POST':
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        gt = request.POST['jobtitle']
        sal = request.POST['salary']
        lo = request.FILES['logo']
        des = request.POST['description']
        exp = request.POST['experience']
        loc = request.POST['location']
        ski = request.POST['skills']
        user = request.user
        recruiter = Recruiters.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, start_date=sd, end_date=ed, title=gt,
            salary=sal, image=lo, description=des, exprience=exp, location=loc, skills=ski, creationdate=date.today())
            error = "no"

        except:
            error="yes"

    d = {'error':error}
    return render(request, 'Recruiters_Login/add_job.html', d)


@login_required
def job_list(request):
    user = request.user
    recruiter = Recruiters.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    context = {'job':job}
    return render(request, 'Recruiters_Login/job_list.html', context)

@login_required
def edit_joblist(request,pk):
    error = ""
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        gt = request.POST['jobtitle']
        sal = request.POST['salary']
        des = request.POST['description']
        exp = request.POST['experience']
        loc = request.POST['location']
        ski = request.POST['skills']
        

        job.title = gt
        job.salary = sal
        job.location = loc
        job.description = des
        job.exprience = exp
        job.skills = ski

        try:
            job.save()
            error = "no"

        except:
            error="yes"

        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass

        if ed:
            try:
                job.end_date = ed
                job.save()
            except:
                pass
        else:
            pass

    d = {'error':error, 'job':job}
    return render(request, 'Recruiters_Login/edit_joblist.html', d)

@login_required
def change_companyLogo(request, pk):
    error = ""
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        cl = request.FILES['logo']
        job.image = cl
        try:
            job.save()
            error = "no"
        except:
            error="yes"


    d = {'error':error, 'job':job}
    return render(request, 'Recruiters_Login/change_companyLogo.html',d)

@login_required
def delete_joblist(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect('Recruiters_Login:job_list')

from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from App_Login.models import UserProfile
from django.contrib.auth.models import User

from userprofile.models import Post

# Create your views here.
@login_required
def home(request):
    return render(request,'userprofile/home.html', context={})

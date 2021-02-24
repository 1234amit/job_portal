from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'job/index.html', context={})

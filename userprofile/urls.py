from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns =[
   path("", views.home, name="home"),
]
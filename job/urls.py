from django.urls import path
from  job import views

app_name = "job"

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('recruiter_login/', views.recruiter_login, name="recruiter_login"),
]
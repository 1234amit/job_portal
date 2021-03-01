from django.urls import path
from Recruiters_Login import views

app_name = "Recruiters_Login"

urlpatterns = [
    path('recruiter_signup/', views.recruiter_signup, name="recruiter_signup"),
    path('recruiter_login/', views.recruiter_login, name="recruiter_login"),
    path('recruiter_home/', views.recruiter_home, name="recruiter_home"),
]
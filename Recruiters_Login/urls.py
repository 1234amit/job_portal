from django.urls import path
from Recruiters_Login import views

app_name = "Recruiters_Login"

urlpatterns = [
    path('recruiter_signup/', views.recruiter_signup, name="recruiter_signup"),
    path('recruiter_login/', views.recruiter_login, name="recruiter_login"),
    path('recruiter_home/', views.recruiter_home, name="recruiter_home"),
    path('recruiter_logout/', views.recruiter_logout, name="recruiter_logout"),
    path('requiterChangePass/', views.requiterChangePass, name="requiterChangePass"),
    path('add_job/', views.add_job, name="add_job"),
    path('job_list/', views.job_list, name="job_list"),
    path('edit_joblist/<int:pk>/', views.edit_joblist, name="edit_joblist"),
    path('delete_joblist/<int:pk>/', views.delete_joblist, name="delete_joblist"),
    path('change_companyLogo/<int:pk>/', views.change_companyLogo, name="change_companyLogo"),
]
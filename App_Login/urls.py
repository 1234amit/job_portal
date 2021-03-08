from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name="edit"),
    path('changepassword/', views.ChangePassword, name="changepassword"),
    path('view_jobs/', views.view_jobs.as_view(), name="view_jobs"),
    path('jobs_details/<int:pk>',views.jobs_details.as_view(), name="jobs_details"),
    path('job_list/', views.job_list, name='job_list'),
    path('delete_jobs/<str:pk>', views.delete_jobs, name='delete_jobs'),
]
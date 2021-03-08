from django.urls import path
from  job import views

app_name = "job"

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('recruiter_login/', views.recruiter_login, name="recruiter_login"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('view_users/', views.view_users, name="view_users"),
    path('delete_user/<int:pk>/', views.delete_user, name="delete_user"),
    path('recruiter_pending/', views.recruiter_pending, name="recruiter_pending"),
    path('change_status/<int:pk>/', views.change_status, name="change_status"),
    path('recruiter_accepted/', views.recruiter_accepted, name="recruiter_accepted"),
    path('recuiter_rejected/', views.recuiter_rejected, name="recuiter_rejected"),
    path('recuiter_all/', views.recuiter_all, name="recuiter_all"),
    path('delete_recruiter/<int:pk>/', views.delete_recruiter, name="delete_recruiter"),
    path('admin_changePass/', views.admin_changePass, name="admin_changePass"),
    path('latest_jobs/', views.latest_jobs, name="latest_jobs"),
    path('total_jobs/', views.total_jobs, name="total_jobs"),

]
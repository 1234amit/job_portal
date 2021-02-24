from django.urls import path
from  job import views

app_name = "job"

urlpatterns = [
    path('', views.index, name="index")
]
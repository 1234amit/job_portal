from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
# Create your models here.
class Recruiters(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=100, null=True)
    Type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username

    


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiters, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100, null=True)
    salary = models.FloatField(max_length=100, null=True)
    image = models.FileField(null=True)
    description = models.CharField(max_length=300, null=True)
    exprience = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=30, null=True)
    skills = models.CharField(max_length=60, null=True)
    creationdate = models.DateField()

    def __str__(self):
        return self.title


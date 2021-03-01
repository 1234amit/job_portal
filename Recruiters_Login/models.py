from django.db import models
from django.contrib.auth.models import User
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

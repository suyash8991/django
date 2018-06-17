from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    address=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    work_experience=models.CharField(max_length=250)
    qualification = models.CharField(max_length=100)

from django.db import models
from django.contrib.postgres.fields import ArrayField
# Creating models

class Users(models.Model):
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=64,null=True)
    email=models.EmailField(max_length=250,null=True)
    accountActive = models.BooleanField(null=True)
    challenges_solved = models.IntegerField(null=True)
    chalsSolvedName = ArrayField(models.CharField(max_length=100,default='none'),null=True)




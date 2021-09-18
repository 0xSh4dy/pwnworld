from django.db import models

# Creating models

class Users(models.Model):
    username=models.CharField(max_length=50,default='invalid')
    password=models.CharField(max_length=64,default='invalid')
    email=models.EmailField(max_length=250,default='invalid@invalid.invalid')
    accountActive = models.BooleanField(default=False)
    challenges_solved = models.IntegerField(default=0)




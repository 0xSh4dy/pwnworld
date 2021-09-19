from django.db import models

# Create your models here.

class WebChallenges(models.Model):
    challengename = models.CharField(max_length=50,default='invalid')
    username = models.CharField(max_length=20,default='invalid')
    password = models.CharField(max_length=64,default='invalid')
    flag = models.CharField(max_length=100,default='invalid')

class Challenges(models.Model):
    challengeName = models.CharField(max_length=50,default='invalid')
    flag = models.CharField(max_length=100,default='invalid')
    solves = models.IntegerField(default=0)
    difficultyLevel = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)



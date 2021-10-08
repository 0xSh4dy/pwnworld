from django.db import models
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField
# Creating models

class Users(models.Model):
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=64,null=True)
    email=models.EmailField(max_length=250,null=True)
    accountActive = models.BooleanField(null=True)
    challenges_solved = models.IntegerField(null=True)
    chals_solved_name = ArrayField(models.CharField(max_length=100,default='none'),null=True)
    attack_attempts = models.IntegerField(null=True)
    is_banned = models.BooleanField(null=True)
    is_challenge_dev = models.BooleanField(null=True)

class Challenges(models.Model):
    challenge_name = models.CharField(max_length=50,null=True)
    challenge_type = models.CharField(max_length=50,null=True)
    challenge_location = models.CharField(max_length=500,null=True)
    flag  = models.CharField(max_length=100,null=True)
    solves = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = JSONField(null=True)
    difficulty = models.CharField(max_length=20,null=True)
    description = models.CharField(max_length=1000,null=True)

class ChallengeDevs(models.Model):
    challenge_author = models.TextField(null=True)
    challenge_name = models.TextField(null=True)
    challenge_flag = models.TextField(null=True)
    challenge_difficulty = models.CharField(max_length=20,null=True)
    challenge_description = models.TextField(null=True)
    
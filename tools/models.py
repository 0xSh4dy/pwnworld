from django.db import models
from django.db.models.fields import CharField, DateField, TextField, TimeField

# Create your models here.
class Notes(models.Model):
    username = CharField(max_length=100,null=True)
    title = TextField(null=True)
    details = TextField(null=True)
    date = DateField(auto_now=False,auto_now_add=False)
    time = TimeField(auto_now=False,auto_now_add=False)

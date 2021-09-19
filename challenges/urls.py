from django.urls import path 
from .views import *
urlpatterns = [
    path('web/baby_s3qu3l',baby_sequel ,name='baby_s3qu3l'),
    path('web/entete',entete,name='entete'),
    path('web/destination/150',destinationContd),
    path('web/destination/<c>',destination,name='destination'),
    path('web/babyAdmin',babyAdmin,name='babyAdmin'),

]

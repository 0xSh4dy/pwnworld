from re import template
from django.urls import path 
from django.conf.urls import url
from django.views.generic.base import TemplateView 
from .views import *
urlpatterns = [
    path('web/baby_s3qu3l',baby_sequel ,name='baby_s3qu3l'),
    path('web/entete',entete,name='entete'),
    path('web/destination/150',destinationContd),
    path('web/destination/<c>',destination,name='destination'),
    path('web/babyAdmin',babyAdmin,name='babyAdmin'),
    path("web/robots.txt",TemplateView.as_view(template_name="web/robots.txt",content_type='text/plain')),
    path('web/w723234',w723234,name='w723234'),
    path('web/whereAreYou',whereAreYou,name='whereAreYou'),
    path('web/kiddo_s3qu3l',kiddo_s3qu3l,name="kiddo_s3qu3l"),
    path('web/baby_ssrf',baby_ssrf,name="baby_ssrf"),
    path('web/baby_ssrf/flag',baby_ssrf_flag,name="baby_ssrf_flag")

]

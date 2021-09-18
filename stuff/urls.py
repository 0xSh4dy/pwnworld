
from django.urls import path,include
from .views import *
urlpatterns = [
    path('register',register ,name='register'),
    path('home',home, name='home'),
    path('',login, name='login'),
    path('confirm/<token>',confirm, name='token')
]

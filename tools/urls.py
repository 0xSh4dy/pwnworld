from django.urls import path
from .views import *


urlpatterns = [
    path('main',main,name='main'),
    path('discussions/',discuss,name='chat'),
    path('notes',notes,name="'notes")
]
from django.urls import path
from .views import *


urlpatterns = [
    path('encDec',encDec,name='encDec'),
    path('discussions/',discuss,name='chat'),
    path('notes',notes,name="'notes")
]
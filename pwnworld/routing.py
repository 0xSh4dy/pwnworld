# chat/routing.py
from django.urls import re_path

from stuff import views
from tools import consumers
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/pwn/(?P<room_name>\w+)/$', views.ChallengeConsumer.as_asgi()),

]
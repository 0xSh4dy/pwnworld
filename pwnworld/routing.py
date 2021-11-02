# chat/routing.py
from django.urls import re_path
from stuff import MainOperations,leaderboard
from stuff.dashboard import DashboardConsumer
from tools import consumers
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/pwn/dashboard', DashboardConsumer.as_asgi()),
    re_path(r'ws/pwn/leaderboard',leaderboard.LeaderboardConsumer.as_asgi()),
    re_path(r'ws/pwn/(?P<room_name>[ -~]+)/$', MainOperations.ChallengeConsumer.as_asgi()),
]

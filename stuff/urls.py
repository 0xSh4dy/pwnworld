
from django.urls import path
from .views import *
urlpatterns = [
    path('register',register ,name='register'),
    path('home',home, name='home'),
    path('signin',signin, name='login'),
    path('leaderboard',leaderboard,name='leaderboard'),
    path('profile/<name>',profile, name='profile'),
    path('',main,name='main'),
    path('confirm/<token>',confirm, name='token'),
    path('logout',logOut,name='logout'),
    path('challenges',challenges,name='challenges'),
    path('challenges/web',web,name='web'),
    path('challenges/cryptography',crypto,name='crypto'),
    path('challenges/pwn',pwn,name='pwn'),
    path('challenges/reversing',rev,name='rev'),
    path('challenges/iot',iot,name='iot'),
    path('challenges/hardware',hardware,name='hardware'),
    path('challenges/jailbreak',jailbreak,name='jailbreak'),
    path('challenges/osint',osint,name='osint'),
    path('challenges/forensics',forensics,name='forensics'),
    path('challenges/misc',misc,name='misc'),
    path('challenges/mixed',mixed,name='mixed'),
    path('reportBugs',report,name='report')
]

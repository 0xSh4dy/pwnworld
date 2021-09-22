
from django.urls import path
from .views import *
urlpatterns = [
    path('register',register ,name='register'),
    path('home',home, name='home'),
    path('signin',signin, name='login'),
    path('confirm/<token>',confirm, name='token'),
    path('logout',logOut,name='logout'),
    path('challenges',challenges,name='challenges'),
    path('challenges/web',web,name='web'),
    path('challenges/crypto',crypto,name='crypto'),
    path('challenges/pwn',pwn,name='pwn'),
    path('challenges/rev',rev,name='rev'),
    path('challenges/iot',iot,name='iot'),
    path('challenges/hardware',logOut,name='hardware'),
    path('challenges/jailbreak',jailbreak,name='jailbreak'),
    path('challenges/osint',osint,name='osint'),
    path('challenges/forensics',forensics,name='forensics'),
    path('challenges/misc',misc,name='misc'),
    path('challenges/mixed',mixed,name='mixed'),
]

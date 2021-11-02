from hashlib import sha256
from django.contrib import auth
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from jwt.exceptions import InvalidSignatureError
from .models import Users,Challenges
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .tokenCreator import generateToken
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import connection
from ratelimit.decorators import ratelimit
from decouple import config
import json
from .ChallengesHandler import ChallsHandler
import jwt
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Users,Challenges, Bugs
from .AuthHandler import AuthHandler
import random,string
cursor = connection.cursor()
regEmail = ""
jwt_secret = config("JWT_SECRET")
room_secret = config("SOCKET_SALT")
authHandler = AuthHandler()
@ratelimit(key='ip',rate='10/h')
def register(request):
    reg = authHandler.register(request)
    return reg

@ratelimit(key='ip',rate='8/m')
def signin(request):
    logIn = authHandler.signin(request)
    return logIn


def main(request):
    return render(request,"signin.html")
def confirm(request,token):
    conf = authHandler.confirm(request,token)
    return conf

def logOut(request):
    logOt = authHandler.logOut(request)
    return logOt




@login_required(login_url='/signin')
def home(request):
    username = request.user.username
    try:
        user_obj = Users.objects.get(username=username)
        solved_chals = user_obj.chals_solved_name
        if solved_chals!=None:
            solved_chals = tuple(solved_chals)
            params = {'solved':solved_chals}
            query = "SELECT challenge_type FROM stuff_challenges WHERE challenge_name in %(solved)s"
            cursor.execute(query,params)
            res = cursor.fetchall()
            dat = '''{"web":"10","pwn":"15","rev":"5","crypto":"9","osint":"12","hardware":"3","misc":"20","jailbreak":"2","forensics":"11"}'''
            diffData = '''{"easy":"20","medium":"15","hard":"5"}'''
        else:
            dat = '''{"web":"0","pwn":"0","rev":"0","crypto":"0","osint":"0","hardware":"0","misc":"0","jailbreak":"0","forensics":"0"}'''
            diffData = '''{"easy":"0","medium":"0","hard":"0"}'''
        resp = render(request,"home.html",{"solved_data":dat,"diffData":diffData})  
        resp.set_cookie("username",username)
        return resp

    except Users.DoesNotExist:
        print("error")    

def report(request):
    if request.user.username == "rakshit":
        query = "SELECT * FROM stuff_bugs;"
        cursor.execute(query)
        res = cursor.fetchall()
        return HttpResponse(res)
    else: 
        if request.method=="POST":
            report = request.POST.get("bug")
            mod = Bugs.objects.create(report = report)
            mod.save()
            return HttpResponse("Thanks for reporting! We'll try to solve that issue")
    
    return render(request,"report.html")
@login_required(login_url='/signin')
def profile(request,name):
    username = request.user.username
    if name==username:
        usr = Users.objects.get(username=username)
        total_solves = usr.challenges_solved
        chals_solved = usr.chals_solved_name
        liked_challenges = usr.liked_challenges
        disliked_challenges = usr.disliked_challenges
        is_online = False
        ret_obj = {"total_solves":total_solves,"chals_solved":chals_solved,"liked_challenges":liked_challenges,"disliked_challenges":disliked_challenges,"created_challenges":0,"is_online":is_online,"username":username}
        ret_obj = json.dumps(ret_obj)
        resp = render(request,"myProfile.html",{"ret_obj":ret_obj})
        resp.set_cookie("username",username)
        return resp
    else:
        try:
            usr = Users.objects.get(username=name)
            total_solves = usr.challenges_solved
            chals_solved = usr.chals_solved_name
            liked_challenges = usr.liked_challenges
            disliked_challenges = usr.disliked_challenges
            is_online = False
            ret_obj = {"total_solves":total_solves,"chals_solved":chals_solved,"liked_challenges":liked_challenges,"disliked_challenges":disliked_challenges,"created_challenges":0,"is_online":is_online,"username":name}

            ret_obj = json.dumps(ret_obj)
            resp = render(request,"profile.html",{"ret_obj":ret_obj})
            resp.set_cookie("username",username)
            return resp
            
        except Users.DoesNotExist:
            return HttpResponse("No user exists with that username")    



# Challenges
@login_required(login_url='/signin')
def challenges(request):
    return render(request,"challenges.html")


@login_required(login_url='/signin')
def leaderboard(request):
    return render(request,"leaderboard.html")
    
# @login_required(login_url="/signin")    
@ratelimit(key='ip',rate='3/m')
def web(request):
    username = request.user.username
    print(username)
    enc_username = jwt.encode({"username":username},jwt_secret,algorithm="HS256").decode()
    query = "SELECT * FROM stuff_challenges WHERE challenge_type='web';"
    cursor.execute(query)
    webChallenges = cursor.fetchall()
    webChals = []
    flagData = []
    # u = User.objects.get(username='rakshit')
    # u.set_password('aaaa')
    # u.save()
    for webChal in webChallenges:
        chal = {
                "challenge_name":webChal[1],
                "challenge_type":"web",
                "difficulty":webChal[7],
                "solves":webChal[3],
                "likes":webChal[4],
                "dislikes":webChal[5],
                "comments":webChal[6],
                "points":webChal[11],
                "description":webChal[9],
                "challenge_location":webChal[10]
                }
        flag = {
            "challenge_name":webChal[1],
            "challenge_flag":webChal[8]
        }
        flagData.append(flag)
        webChals.append(chal)
    s2 = ''.join(random.choices(string.ascii_letters+string.digits,k=10))
    r1 =  enc_username + room_secret + s2
    r1 = sha256(r1.encode()).hexdigest()
    typeData= {"cat":"Web_Exploitation","challenges":webChals}
    resp = render(request,"challs.html",typeData)
    resp.set_cookie("auth",enc_username)
    resp.set_cookie("r1",r1)
    return resp

@ratelimit(key='ip',rate='10/m',method=ratelimit.ALL)
@login_required(login_url="/signin")    
def crypto(request):
    typeData= {"cat":"Cryptography"}
    was_limited = getattr(request, 'limited', False)
    print(was_limited)
    if was_limited:
        return HttpResponse("DoS attack discovered. Your IP address has been noted.")
    else:
        return render(request,"challs.html",typeData)

@ratelimit(key='user_or_ip',rate='10/m')
@login_required(login_url="/signin")    
def pwn(request):
    typeData= {"cat":"pwn"}
    return render(request,"challs.html",typeData)
    
@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def rev(request):
    typeData= {"cat":"Reverse-Engineering"}
    return render(request,"challs.html",typeData)

@ratelimit(key='user_or_ip',rate='3/m')    
@login_required(login_url="/signin")    
def iot(request):
    typeData= {"cat":"IoT"}
    return render(request,"challs.html",typeData)
    
@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def forensics(request):
    typeData= {"cat":"Forensics"}
    return render(request,"challs.html",typeData)
    
@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def jailbreak(request):
    typeData= {"cat":"Jailbreak"}
    return render(request,"challs.html",typeData)
    
@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def osint(request):
    typeData= {"cat":"OSINT"}
    return render(request,"challs.html",typeData)
    
@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def hardware(request):
    typeData= {"cat":"Hardware"}
    return render(request,"challs.html",typeData)

@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def misc(request):
    typeData= {"cat":"Miscellaneous"}
    return render(request,"challs.html",typeData)

@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def mixed(request):
  
    typeData= {"cat":"Mixed"}
    return render(request,"challs.html",typeData)
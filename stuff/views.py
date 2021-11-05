from hashlib import sha256
from django.contrib import auth
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from jwt.exceptions import InvalidSignatureError
from .models import Users,Challenges
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .tokenCreator import JWT_SECRET, generateToken
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



# @login_required(login_url='/signin')
def home(request):
    username = request.user.username
    try:
        user_obj = Users.objects.get(username=username)
        solved_chals = user_obj.chals_solved_name
        print(len(solved_chals))
        if len(solved_chals)!=0:
            solved_chals = tuple(solved_chals)
            params = {'solved':solved_chals}
            query = "SELECT challenge_type FROM stuff_challenges WHERE challenge_name in %(solved)s"
            cursor.execute(query,params)
            res = cursor.fetchall()
            print(res)
            countWeb=0;countPwn=0;countRev=0;countCrypto=0;countOsint=0;countHardware=0;countMisc=0;countJailbreak=0;countForensics=0;
            for r in res:
                if r[0]=='web':
                    countWeb+=1
                elif r[0]=='pwn':
                    countPwn+=1
                elif r[0]=='rev':
                    countRev+=1
                elif r[0]=='crypto':
                    countCrypto+=1
                elif r[0]=='osint':
                    countOsint+=1
                elif r[0]=='hardware':
                    countHardware+=1
                elif r[0]=='forensics':
                    countForensics+=1
                elif r[0]=='misc':
                    countMisc+=1
                elif r[0]=='jailbreak':
                    countJailbreak+=1    
            
            dat = {"web":countWeb,"pwn":countPwn,"rev":countRev,"crypto":countCrypto,"osint":countOsint,"hardware":countHardware,"misc":countMisc,"jailbreak":countJailbreak,"forensics":countForensics}
            dat = json.dumps(dat)
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
# @login_required(login_url='/signin')
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
# @login_required(login_url='/signin')
def challenges(request):
    return render(request,"challenges.html")


# @login_required(login_url='/signin')
def leaderboard(request):
    return render(request,"leaderboard.html")
    
# @login_required(login_url="/signin")    
# @ratelimit(key='ip',rate='3/m')
def renderChallenges(req,type):
    username = req.user.username
    # print(username)
    enc_username = jwt.encode({"username":username},jwt_secret,algorithm="HS256")
    query = "SELECT * FROM stuff_challenges WHERE challenge_type='{}';".format(type)
    cursor.execute(query)
    Challenges = cursor.fetchall()
    Chals = []
    flagData = []
    # u = User.objects.get(username='rakshit')
    # u.set_password('aaaa')
    # u.save()
    for Chal in Challenges:
        chal = {
                "challenge_name":Chal[1],
                "challenge_type":"web",
                "difficulty":Chal[7],
                "solves":Chal[3],
                "likes":Chal[4],
                "dislikes":Chal[5],
                "comments":Chal[6],
                "points":Chal[11],
                "description":Chal[9],
                "challenge_location":Chal[10]
                }
        flag = {
            "challenge_name":Chal[1],
            "challenge_flag":Chal[8]
        }
        flagData.append(flag)
        Chals.append(chal)
    s2 = ''.join(random.choices(string.ascii_letters+string.digits,k=10))
    r1 =  enc_username + room_secret + s2
    r1 = sha256(r1.encode()).hexdigest()
    fi_id = ''
    if type=='web':
        typeData= {"cat":"Web_Exploitation","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"web"},JWT_SECRET,algorithm="HS256")

    elif type=='pwn':
        typeData= {"cat":"pwn","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"pwn"},JWT_SECRET,algorithm="HS256")

    elif type=='forensics':
        typeData= {"cat":"Digital_Forensics","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"forensics"},JWT_SECRET,algorithm="HS256")

    elif type=='rev':
        typeData= {"cat":"Reverse_Engineering","challenges":Chals}
        fi_id=jwt.encode({"rev":"web"},JWT_SECRET,algorithm="HS256")

    elif type=='crypto':
        typeData= {"cat":"Cryptography","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"crypto"},JWT_SECRET,algorithm="HS256")

    elif type=='network':
        typeData= {"cat":"Networking","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"network"},JWT_SECRET,algorithm="HS256")

    elif type=='hardware':
        typeData= {"cat":"Hardware","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"hardware"},JWT_SECRET,algorithm="HS256")

    elif type=='osint':
        typeData= {"cat":"OSINT","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"osint"},JWT_SECRET,algorithm="HS256")

    elif type=='jailbreak':
        typeData= {"cat":"Jailbreak","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"jailbreak"},JWT_SECRET,algorithm="HS256")

    elif type=='misc':
        typeData= {"cat":"Misc","challenges":Chals}
        fi_id=jwt.encode({"currentPage":"misc"},JWT_SECRET,algorithm="HS256")

            
    resp = render(req,"challs.html",typeData)
    resp.set_cookie("auth",enc_username)
    resp.set_cookie("r1",r1)
    resp.set_cookie("fi_id",fi_id)
    return resp

def web(request):
    res = renderChallenges(request,'web')
    return res    


@ratelimit(key='ip',rate='10/m',method=ratelimit.ALL)
# @login_required(login_url="/signin")    
def crypto(request):
    res = renderChallenges(request,'crypto')
    return res

@ratelimit(key='user_or_ip',rate='10/m')
# @login_required(login_url="/signin")    
def pwn(request):
    res = renderChallenges(request,'pwn')    
    return res

@ratelimit(key='user_or_ip',rate='3/m')
@login_required(login_url="/signin")    
def rev(request):
    res = renderChallenges(request,'rev')
    return res


@ratelimit(key='user_or_ip',rate='3/m')    
# @login_required(login_url="/signin")    
def network(request):
    res = renderChallenges(request,'network')
    return res
    
@ratelimit(key='user_or_ip',rate='3/m')
# @login_required(login_url="/signin")    
def forensics(request):
    res = renderChallenges(request,'forensics')
    return res
    
@ratelimit(key='user_or_ip',rate='3/m')
# @login_required(login_url="/signin")    
def jailbreak(request):
    res = renderChallenges(request,'jailbreak')
    return res
    
@ratelimit(key='user_or_ip',rate='3/m')
# @login_required(login_url="/signin")    
def osint(request):
    res = renderChallenges(request,'osint')
    return res
    
@ratelimit(key='user_or_ip',rate='3/m')
# @login_required(login_url="/signin")    
def hardware(request):
    res = renderChallenges(request,'hardware')
    return res

@ratelimit(key='user_or_ip',rate='3/m')
# @login_required(login_url="/signin")    
def misc(request):
    res = renderChallenges(request,'misc')
    return res


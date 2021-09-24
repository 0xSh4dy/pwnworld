from hashlib import sha256
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Users,Challenges
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .tokenCreator import generateToken
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import connection

cursor = connection.cursor()
regEmail = ""
def register(request):
    username = request.POST.get('username',"demoName")
    password = request.POST.get('password',"noPass")
    email = request.POST.get("email","someEmail")
    emailTaken = False
    usernameTaken = False
    accountInactive = True
    global regEmail
    regEmail = email
    if username!="demoName" and password!="noPass" and email!="someEmail":
        try: 
            usr1 = Users.objects.get(username=username)
            if usr1.username == username:
                usernameTaken=True
        except Users.DoesNotExist:
            usernameTaken=False    
        if usernameTaken:
            return HttpResponse("Username is already taken by someone")
        else:    
            try:
                usr = Users.objects.get(email=email)
                if usr.accountActive==True:
                    accountInactive=False
                if usr.email==email:
                    emailTaken=True    
                
            except Users.DoesNotExist:
                 emailTaken = False
            if emailTaken==False and accountInactive:
                password = sha256(password.encode()).hexdigest()
                print(username,password,email)
                user = Users(username=username,password=password,email=email,accountActive=False)

            # Send the email
                subject = "Account confirmation"
            
                token = generateToken(email)
                url = 'http://localhost:8000/confirm/{}'.format(token)
                message = render_to_string('regEmail.html',{'link':url})
                plain_message = strip_tags(message)
                from_email = 'pwnworld10@gmail.com'
                to = email
                send_mail(subject,plain_message,from_email,[to],html_message=message)
                user.save()
                return HttpResponse('Confirmation mail sent')
            elif emailTaken==True and accountInactive:
                subject = "Account confirmation"
                token = generateToken(email)
                url = 'http://localhost:8000/confirm/{}'.format(token)
                message = render_to_string('regEmail.html',{'link':url})
                plain_message = strip_tags(message)
                from_email = 'pwnworld10@gmail.com'
                to = email
                send_mail(subject,plain_message,from_email,[to],html_message=message)
                return HttpResponse('Confirmation mail sent')
            elif emailTaken and accountInactive==False:
                return HttpResponse("Email is already taken")    

    else:
        return render(request,"register.html")  


def signin(request):
    if request.POST:
        email = request.POST.get('email','invalid')
        password = request.POST.get('password','invalid')
        password = sha256(password.encode()).hexdigest()
        try:
            user = Users.objects.get(email=email)
            if user.accountActive==True:
                email = user.email
                username = user.username
                
                authUser =authenticate(request,username=username,password=password)
                if authUser is not None:
                    login(request,authUser)
                    return redirect("/home")
                else:
                    return HttpResponse("Invalid credentials")  

            else:
                return HttpResponse("Your account is not activated. Please check the email sent before. If it does not work, register again")    
        except Users.DoesNotExist:
            return HttpResponse("Account with that email does not exist")
    return render(request,"signin.html")


def main(request):
    return render(request,"main.html")
def confirm(request,token):
    try:
        user = Users.objects.get(email=regEmail)
        if user.accountActive==False:
            user.accountActive = True
            user.save()
            username = user.username
            password = user.password
            email = user.email
            userAuth = User.objects.create_user(username,email,password)
            userAuth.save()
    except Users.DoesNotExist:
        return HttpResponse("Either your account has been activated or there was some error")  
    return HttpResponse("Account confirmed! Go to the homepage and signin")

def logOut(request):
    logout(request)
    return redirect("/signin")

@login_required(login_url='/signin')
def home(request):
    return render(request,"home.html")  


# Challenges
@login_required(login_url='/signin')
def challenges(request):
    return render(request,"challenges.html")


@login_required(login_url="/signin")    
def web(request):
    query = "SELECT * FROM stuff_challenges WHERE challenge_type='web';"
    cursor.execute(query)
    webChallenges = cursor.fetchall()
    webChals = []
    flagData = []
    for webChal in webChallenges:
        chal = {
                "challenge_name":webChal[1],
                "challenge_type":"web",
                "difficulty":webChal[7],
                "solves":webChal[3],
                "likes":webChal[4],
                "dislikes":webChal[5],
                "comments":webChal[6],
                "description":webChal[9],
                "challenge_location":webChal[10]
                }
        flag = {
            "challenge_name":webChal[1],
            "challenge_flag":webChal[8]
        }
        flagData.append(flag)
        webChals.append(chal)

    typeData= {"cat":"Web-Exploitation","challenges":webChals}
    return render(request,"challs.html",typeData)

@login_required(login_url="/signin")    
def crypto(request):
    typeData= {"cat":"Cryptography"}
    return render(request,"challs.html",typeData)

@login_required(login_url="/signin")    
def pwn(request):
    typeData= {"cat":"pwn"}
    return render(request,"challs.html",typeData)
    
@login_required(login_url="/signin")    
def rev(request):
    typeData= {"cat":"Reverse-Engineering"}
    return render(request,"challs.html",typeData)
    
@login_required(login_url="/signin")    
def iot(request):
    typeData= {"cat":"IoT"}
    return render(request,"challs.html",typeData)
    
@login_required(login_url="/signin")    
def forensics(request):
    typeData= {"cat":"Forensics"}
    return render(request,"challs.html",typeData)
    
@login_required(login_url="/signin")    
def jailbreak(request):
    typeData= {"cat":"Jailbreak"}
    return render(request,"challs.html",typeData)
    
@login_required(login_url="/signin")    
def osint(request):
    typeData= {"cat":"OSINT"}
    return render(request,"challs.html",typeData)
    
@login_required(login_url="/signin")    
def hardware(request):
    typeData= {"cat":"Hardware"}
    return render(request,"challs.html",typeData)

@login_required(login_url="/signin")    
def misc(request):
    typeData= {"cat":"Miscellaneous"}
    return render(request,"challs.html",typeData)


@login_required(login_url="/signin")    
def mixed(request):
  
    typeData= {"cat":"Mixed"}
    return render(request,"challs.html",typeData)
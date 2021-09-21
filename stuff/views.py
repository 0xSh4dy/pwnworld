from hashlib import sha256
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Users
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .tokenCreator import generateToken
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
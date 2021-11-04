from hashlib import sha256,sha1
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Users,Events
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
import jwt
import requests ,datetime
cursor = connection.cursor()
JWT_SECRET = config("JWT_SECRET")
class AuthHandler:
    def register(self,request):
        if request.POST:
            username = request.POST.get('username',"demoName")
            password = request.POST.get('password',"noPass")
            email = request.POST.get("email","someEmail")
            clientkey = request.POST["g-recaptcha-response"]
            secretKey = config("RECAPTCHA_PRIVATE_KEY")
            captcha = {"secret":secretKey,"response":clientkey}
            res = requests.post(url="https://www.google.com/recaptcha/api/siteverify",data=captcha).text
            res = json.loads(res)
           
            global regEmail
            regEmail = email
            registerOrNot = False
            if(res.get('success')==True):
                if username=="demoName" or password=="noPass" or email=="someEmail":
                    return HttpResponse("There was some error, we'll look into it")
                else:
                    user = Users.objects.filter(username=username)
                    if user.exists()==True:
                        if(Users.objects.get(username=username).email==None):
                            user.delete()
                        else:    
                            return HttpResponse("Username is already taken")
                    elif user.exists()==False:
                        uEm = Users.objects.filter(email=email)
                        if uEm.exists()==True:
                            if Users.objects.get(email=email).username==None:
                                uEm.delete()
                                registerOrNot=True
                            else:
                                return HttpResponse("Email is already taken")    
                        else:    
                            registerOrNot = True

                if registerOrNot==True:
                    usrObj = Users.objects.create(username=username)
                    usrObj.email = email
                    usrObj.password = sha256(password.encode()).hexdigest()
                    usrObj.accountActive = False
                    usrObj.challenges_solved = 0
                    usrObj.chals_solved_name = []
                    usrObj.liked_challenges = []
                    usrObj.disliked_challenges = []
                    usrObj.total_points = 0
                    subject = "Account confirmation"
                    token = generateToken(email)
                    url = 'http://127.0.0.1:8001/confirm/{}'.format(token)
                    message = render_to_string('regEmail.html',{'link':url})
                    plain_message = strip_tags(message)
                    from_email = 'pwnworld10@gmail.com'
                    to = email
                    try:
                        send_mail(subject,plain_message,from_email,[to],html_message=message)
                        usrObj.save()
                        return HttpResponse("Account verification email sent. Check your email. Do not forget to check the spam folder")
                    except Exception as e:
                        print(e)
                        return HttpResponse("Internal server error")

                    
                else:
                    return HttpResponse("Either the username or the email is already taken")
            else:
                return HttpResponse("Recaptcha validation failed")             

        else:
            return render(request,"register.html")  



# Signin
    def signin(self,request):
        if request.POST:
            email = request.POST.get('email','invalid')
            password = request.POST.get('password','invalid')
            password = sha256(password.encode()).hexdigest()
            # password = sha256(password.encode()).hexdigest()

            # Recaptcha validation
            clientkey = request.POST["g-recaptcha-response"]
            secretKey = config("RECAPTCHA_PRIVATE_KEY")
            captcha = {"secret":secretKey,"response":clientkey}
            res = requests.post(url="https://www.google.com/recaptcha/api/siteverify",data=captcha).text
            res = json.loads(res)

            if(res.get('success')==True):
                try:
                    user = Users.objects.get(email=email)
                    if user.accountActive==True:
                        email = user.email
                        username = user.username
                        print(username)
                        print(email)
                        authUser =authenticate(request,username=username,password=password)
                        if authUser is not None:
                            login(request,authUser)
                            resp =  redirect("/home")
                            resp.set_cookie("username",username)
                            return resp
                        else:
                            return HttpResponse("Invalid credentials")  

                    else:
                        return HttpResponse("Your account is not activated. Click <a href='/confirmPage' >here</a>to generate a new verification email")    
                except Users.DoesNotExist:
                    return HttpResponse("Account with that email does not exist")
            else:
                return HttpResponse("Recaptcha validation failed")
        return render(request,"signin.html")


    def main(self,request):
        return render(request,"main.html")

    # def regenerateToken(self,request):
    #     subject = "Account confirmation"
    #     token = generateToken(email)
    #     url = 'http://localhost:8000/confirm/{}'.format(token)
    #     message = render_to_string('regEmail.html',{'link':url})
    #     plain_message = strip_tags(message)
    #     from_email = 'pwnworld10@gmail.com'
    #     to = email
    #     send_mail(subject,plain_message,from_email,[to],html_message=message)
    #     user.save()
    #     return HttpResponse('Confirmation mail sent')  
    
    def confirm(self,request,token):
        jwtToken = request.path[9:]
        dec = ''
        try:
            dec = jwt.decode(jwt=jwtToken,key=JWT_SECRET,algorithms=["HS256"])
        except Exception:
            return HttpResponse("Invalid url")
        email = dec.get('email')
        try:
            user = Users.objects.get(email=email)
            if user.accountActive==False:
                user.accountActive = True
                user.save()
                username = user.username
                password = user.password
                email = user.email
                userAuth = User.objects.create_user(username,email,password)
                userAuth.save()
                event = Events.objects.create(username=username)                
                event.timing = str(datetime.datetime.now().replace(microsecond=0))
                event.eventData = "{} joined pwnworld!".format(username)
                event.save()
                return HttpResponse("Account confirmed! Go to the <a href='/signin'>homepage</a> and signin")
            else:
                return HttpResponse("Your account has already been verified")    
        except Users.DoesNotExist:
            return HttpResponse("No account exists with such email")  

    def logOut(self,request):
        logout(request)
        return redirect("/signin")
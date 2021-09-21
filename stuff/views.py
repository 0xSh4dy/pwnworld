from hashlib import sha256
from django.shortcuts import render,HttpResponse,redirect
from .models import Users
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .tokenCreator import generateToken
from django.contrib import messages
regEmail = ""
def register(request):
    username = request.POST.get('username',"demoName")
    password = request.POST.get('password',"noPass")
    email = request.POST.get("email","someEmail")
    emailTaken = False
    if username!="demoName" and password!="noPass" and email!="someEmail":
        try:
            usr = Users.objects.get(email=email)
            print(usr.username,usr.email)

            emailTaken=True
        except Users.DoesNotExist:
            emailTaken = False
        if emailTaken==False:
            password = sha256(password.encode()).hexdigest()
            print(username,password,email)
            user = Users(username=username,password=password,email=email,accountActive=False)

            # Send the email
            subject = "Account confirmation"
            global regEmail
            regEmail = email
            token = generateToken(email)
            url = 'http://localhost:8000/confirm/{}'.format(token)
            message = render_to_string('regEmail.html',{'link':url})
            plain_message = strip_tags(message)
            from_email = 'pwnworld10@gmail.com'
            to = email
            send_mail(subject,plain_message,from_email,[to],html_message=message)
            user.save()
            return HttpResponse('Confirmation mail sent')
        else:
            return HttpResponse("Email is already taken")    

    else:
        return render(request,"register.html")  


def signin(request):
    email = request.POST.get('email','invalid')
    password = request.POST.get('password','invalid')
    if request.POST:
        try:
            user = Users.objects.get(email=email)
            if user.accountActive==True:
                return HttpResponse(user)
            else:
                return HttpResponse("Account not activated")    
                
        except Users.DoesNotExist:
            return HttpResponse("Account with that email does not exist")
    return render(request,"signin.html")

def home(request):
    return render(request,"home.html")

def confirm(request,token):
    try:
        print(regEmail)
        user = Users.objects.get(email=regEmail)
        user.accountActive = True
        user.save()
    except Users.DoesNotExist:
        return HttpResponse("There was some error,please try again")  
    return HttpResponse("Account confirmed! Go to the homepage and signin")

    
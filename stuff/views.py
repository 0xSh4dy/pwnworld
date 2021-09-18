from django.shortcuts import render,HttpResponse,redirect
# from .models import Users
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .tokenCreator import *

def register(request):
    username = request.POST.get('username',"demoName")
    password = request.POST.get('password',"noPass")
    email = request.POST.get("email","someEmail")
    if username!="demoName" and password!="noPass" and email!="someEmail":
        print(username,password,email)
        # user = Users(username=username,password=password,email=email,accountActive=False)

        # Send the email
        # subject = "Account confirmation"
        # token = geneateToken(email)
        # url = 'http://localhost:8001/confirm/{}'.format(token)
        # message = render_to_string('regEmail.html',{'link':url})
        # plain_message = strip_tags(message)
        # from_email = 'pwnworld10@gmail.com'
        # to = 'rakshitawasthi17@gmail.com'
        # send_mail(subject,plain_message,from_email,[to],html_message=message)
        # user.save()
        return HttpResponse('Confirmation mail sent')

    else:
        return render(request,"register.html")  


def login(request):
    # username = request.POST.get('username','invalid')
    # password = request.POST.get('password','invalid')
    # user = Users(username=username,password=password)
    # print(user)
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def confirm(request,token):
    return redirect("/login")

    
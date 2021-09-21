from django.db.utils import ProgrammingError
from django.shortcuts import render,HttpResponse,redirect
from django.db import connection
# from .models import WebChallenges
from django.contrib import messages
from hashlib import md5
# Create your views here.
cursor = connection.cursor()


# Web Challenges
# Note: Challenges related to Apache2 and php are not here, they are in a directory called web_php 
# which will be served using an Apache2 server running on Ubuntu

# Challenge1 : baby_s3qu3l
def baby_sequel(request):
    pass
#     if request.POST:
#         username = request.POST.get("username","invalid")
#         password = request.POST.get("password","invalid")
#         try:
#             query = '''SELECT * FROM challenges_webchallenges where username='{}' and password='{}';'''.format(username,password)
#             cursor.execute(query)
#             response = cursor.fetchone()[4]
#             if "flag" in response:
#                 return HttpResponse(response)
#         except TypeError:
#             return HttpResponse("Invalid credentials")        
#         except ProgrammingError:
#             return HttpResponse("Invalid SQL syntax")      
#     return render(request,"baby_s3qu3l.html") 


# Challenge2 : entête
def entete(request):
    requestHeaders = request.headers

    acceptLanguage = requestHeaders.get('Accept-Language')
    referer = requestHeaders.get('Referer')
    userAgent = requestHeaders.get('User-Agent')
    if acceptLanguage=="fr" and referer=="http://localhost:8000/challenges/web/entete" and userAgent=="pwnbrowser":
        resp = "Take your flag:  flag{hmm_y0u_kn0w_ab0u7_http_h34d3r5_isdnfeisj}"
        return HttpResponse(resp)

    return render(request,"entete.html")

# Challenge3: Destination

def destination(request,c):
    for i in range(26):
        response = redirect("/challenges/web/destination/{}".format(i))
        if i==0:
            response.set_cookie('Message','MTUwIGlzIG15IGZhdm9yaXRlIG51bWJlci4gQnV0IEkgaGF0ZSAw')
        return response    

def destinationContd(request):
    return HttpResponse("flag{h3h3_s0_m4ny_r3d1r3c7s_awjndskf3fnd}")

# Challenge4: babyAdmin
def babyAdmin(request):
    response = render(request,"babyAdmin.html")
    response.set_cookie('user','334c4a4c42fdb79d7ebc3e73b517e6f8')
    if request.POST:
        cookie = str(request.COOKIES['user'])
        cookieValue = cookie
        adminCookie = md5('admin'.encode()).hexdigest()
        if cookieValue==adminCookie:
            return render(request,"babyAdmin1.html",{'resp':'flag{w3lc0m3_t0_th3_s1t3_mr_4dm1n_imdf5r55r444fg}'})
        else:
            username = str(request.POST.get('username'))
            username = username.lower()
            respText = ''
            if username == "admin":
                respText="Sorry, you are not admin"
            else:
                respText = "Welcome to my site, {} ".format(username)  
            cookieValue = md5(username.encode()).hexdigest()    
            response1 =  render(request,"babyAdmin1.html",{'resp':respText})
            if username!="admin":
                response1.set_cookie("user",cookieValue)      
            return response1
    return response


# Challenge5: Where are you?
def whereAreYou(request):
    return render(request,"whereAreYou.html")
def w723234(request):
    return render(request,"w723234.html")

#Challenge6: kiddo_s3qu3l
def kiddo_s3qu3l(request):
    pass
#     if request.POST:
#         username = str(request.POST.get('username'))
#         password = str(request.POST.get('password'))
#         blackword = 'admin'
#         if blackword in username:
#             username = username.replace(blackword,'')
#         query = '''SELECT * FROM kiddo_s3qu3l where username='{}' and password='{}';'''.format(username,password)
#         try:
#             cursor.execute(query)
#             result = cursor.fetchone()[4]
#             if result!=None:
#                 return HttpResponse(result)
#             else:
#                 return HttpResponse("Invalid credentials")    
#         except ProgrammingError:
#             return HttpResponse("You have some error in your SQL syntax")
#         except TypeError:
#             return HttpResponse("Invalid credentials")    
#     return render(request,"kiddo_s3qu3l.html")    



        





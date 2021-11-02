from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
import json
import hashlib
import binascii
import base64
from .models import Notes
import datetime
import random,string
from hashlib import sha256
cursor = connection.cursor()
# @login_required(login_url='http://127.0.0.1:8000/signin')
def encDec(request):
    if request.method=="POST":
        data = json.loads(request.body.decode())
        val1 = str(data.get("val1"))
        val2 = data.get("val2")
        answer = ""
        if val2=="base32encode":
            answer = base64.b32encode(val1.encode()).decode()
        elif val2=="base32decode":
            try:
                answer = base64.b32decode(val1.encode()).decode()    
            except Exception:
                answer= "Invalid base32 data" 
        elif val2 == "toHex":
            try:
                answer = binascii.hexlify(val1.encode()).decode()
            except Exception:
                answer = "Invalid data"    
        elif val2 == "fromHex":
            try:
                answer = binascii.unhexlify(val1.encode()).decode()
            except Exception:
                answer = "Invalid data"    
        elif val2 == "decodeBS":
            try:
                answer =  binascii.unhexlify((hex(int(val1,2))[2:]).encode()).decode()
            except Exception:
                answer = "There is some problem with the binary string provided by you"
        elif val2 == "toBS":
            try:
                answer = binascii.hexlify(val1.encode()).decode()
                answer = int(answer,16)
                answer = bin(answer)
                print(answer)
            except Exception:
                answer = "Invalid input"    
        return HttpResponse(answer)
        
    return render(request,"encDec.html")

# @login_required(login_url='http://127.0.0.1:8000/signin')
def discuss(request):
    user = str(request.user)
    randString = ''.join(random.choices(string.ascii_letters+string.digits ,k=20))
    nonce = sha256(randString.encode()).hexdigest()
    response = render(request,"discuss.html",{'user':user,'nonce':nonce})
    response.headers["Content-Security-Policy"] = "default-src 'none'; connect-src 'self'; img-src 'self'; script-src 'nonce-{}' 'self'; style-src 'self' 'nonce-{}'; form-action 'none';frame-src 'none'; media-src 'none'; object-src 'none'; ".format(nonce,nonce)
    return response   

# @login_required(login_url='http://127.0.0.1:8000/signin')
def notes(request):
    username = str(request.user)
    if request.method=="POST":
        username = str(request.user)
        title = request.POST.get("title","invalid")
        details = request.POST.get("details","invalid")
        curDate = datetime.date.today()
        curTime = datetime.datetime.now().strftime("%H:%M:%S")
        try:
            sampleNote = Notes.objects.get(title=title)
            print("Note with that title already exists")
        except Notes.DoesNotExist:
            note = Notes.objects.create(username=username,title=title,details=details,date=curDate,time=curTime)
            note.save()
        
        messages.success(request,"New note created")
        

    elif request.method=="PATCH":
        data = json.loads(request.body.decode())
        title = data.get('title')
        details = data.get('details')
        note = Notes.objects.get(title=title)
        note.details = details
        note.date = datetime.date.today()
        print(datetime.datetime.now())
        note.time = datetime.datetime.now().strftime("%H:%M:%S")
        note.save()
        messages.add_message(request, messages.INFO, 'Hello world.') 
    elif request.method=="DELETE":
        data = json.loads(request.body.decode())
        title = data.get('title')   
        note = Notes.objects.filter(title=title)
        note.delete()
       
    query = "SELECT * from tools_notes where username='{}'".format(username)
    noteData = []
    cursor.execute(query)
    result = cursor.fetchall() 
    for res in result:
        singleNote = {"title":res[1]
                        ,"details":res[2],
                        "date":res[3],
                        "time":res[4]
                        }
        noteData.append(singleNote)                
    return render(request,"notes.html",{'data':noteData})        
     
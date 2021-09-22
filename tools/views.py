from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
import json
import hashlib
import binascii
import base64

@login_required(login_url='http://127.0.0.1:8000/signin')
def main(request):
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
        
    return render(request,"main.html")

@login_required(login_url='http://127.0.0.1:8000/signin')
def discuss(request):
    user = str(request.user)
    response = render(request,"discuss.html",{'user':user})
    return response    
        
     
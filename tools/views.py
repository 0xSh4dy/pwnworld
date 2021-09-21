from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
import json
import hashlib
import base64
# Create your views here.

# @login_required(login_url='http://127.0.0.1:8000/signin')
def main(request):
    if request.method=="POST":
        data = json.loads(request.body.decode())
        val1 = data.get("val1")
        val2 = data.get("val2")
        answer = ""
        if val2=="base32encode":
            answer = base64.b32encode(val1.encode()).decode()
        elif val2=="base32decode":
            try:
                answer = base64.b32decode(val1.encode()).decode()    
            except Exception:
                answer= "Invalid base32 data"    
        return HttpResponse(answer)
    return render(request,"main.html")
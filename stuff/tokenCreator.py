from hashlib import sha1
from datetime import datetime, time
from decouple import config
JWT_SECRET = config("JWT_SECRET")
import jwt
def generateToken(email):
    timeStamp = datetime.now()
    token = str(timeStamp)+email
    token = jwt.encode({"email":email},JWT_SECRET,algorithm="HS256")
    return token
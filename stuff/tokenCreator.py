from hashlib import sha1
from datetime import datetime, time
def tokenCreator(email):
    timeStamp = datetime.now()
    token = str(timeStamp)+email
    token = sha1(token)
    return token
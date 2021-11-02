from channels.generic.websocket import AsyncWebsocketConsumer
from .ChallengesHandler import ChallsHandler
import jwt
import json
from jwt import InvalidSignatureError
from decouple import config
from hashlib import sha256
import random,string
jwt_secret = config("JWT_SECRET")
room_secret = config("SOCKET_SALT")
class ChallengeConsumer(AsyncWebsocketConsumer,ChallsHandler):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        s2 = ''.join(random.choices(string.ascii_letters+string.digits,k=10))
        room_group = str(self.room_name) + room_secret + s2
        room_group = sha256(room_group.encode()).hexdigest()
        self.room_group_name = room_group
        self.function='none'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
# Disconnect
    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )  
# Receive message from WebSocket
    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        try:
            message = text_data_json.get('message')
            user = text_data_json.get('user')
            try:
                self.username = jwt.decode(user,jwt_secret,algorithms=["HS256"])
                print(self.username)
                
                data = text_data_json.get('data')
                challenge_name = text_data_json.get('challenge_name')
                flag = text_data_json.get('flag')
                comment = text_data_json.get('comment')
                
                filter = text_data_json.get('filter')
                print(filter)
                self.handler = ChallsHandler(username=user)
                self.result = ''
                res = ' '
                challenge_type = text_data_json.get('challenge_type')
      
                if message=='like':
                    res = await self.handler.likeOrDislike("like",challenge_name,user)
                    self.function = 'like'
                elif message=='dislike':
                    res = await self.handler.likeOrDislike("dislike",challenge_name,user)
                    self.function='dislike'
                elif message=='submit_flag':
                    res = await self.handler.checkFlag(flag,challenge_name,user)
                    self.function='checkFlag'
                elif message=='comment':
                    res = await self.handler.comment(comment,challenge_name,user)
                    self.function='comment'
                elif message=='filter':
                    res = await self.handler.filter(filter,user)    
                    self.function ='filter'
                self.result = res
            except InvalidSignatureError:
                self.username='Invalid'
                self.result='Invalid auth token'
                self.function = 'Invalid'
                self.validUser = "no"
            # if jwt.decode(user,jwt_secret,algorithms=["HS256"]).username=='':
            #     print("Fake username")
            # else:
            #     print("Real username")
            #     print(jwt.decode(user,jwt_secret,algorithms=["HS256"]))    
            #     print(jwt.decode(user,jwt_secret,algorithms=["HS256"]).username.length)    

        except Exception as e:
            print(str(e))
            self.username='Invalid'
            self.function = 'Invalid'
            self.result = 'Invalid operation or invalid auth token'

        

        #  ALERT : ADD SQL INJECTION PROTECTION HERE
        # if res==True:
        #     try:
        #         query = "SELECT * FROM pwnworld_challenges where challenge_type='{}'".format(challenge_type)
        #         cursor.execute(query)
        #         self.result = cursor.fetchall()
        #     except Exception:
        #         self.result = "Failed to execute the operation"

        # elif res==False:
        #     self.result = "Failed to execute the operation"
        # else:
        #     self.result = res
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
                {
                    'type':'chat_message',
                    'message':self.result,
                    'function':self.function,
                    'user':self.username
                }
            )
        
                  
    
    # Receive message from room group
    async def chat_message(self,event):
        # message = event['message']
        # user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': self.result,
            'function':self.function,
            'user':self.username
        }))
       

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Events
from django.db import connection
from decouple import config
cursor = connection.cursor()
class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'dashboard'
        self.room_group_name = 'pwn_dashboard'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )    

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        query = "SELECT * FROM stuff_events ORDER BY id DESC LIMIT 20;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'chat_message',
                'data':result
            }
        )
    
    async def chat_message(self,event):
        data = event.get('data')
        await self.send(text_data=json.dumps({
            'type':'chat_message',
            'data':data
        }
        ))


from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.db import connection
from .models import Users
from asgiref.sync import sync_to_async

cursor = connection.cursor()

@sync_to_async
def fetchData():
    query = "SELECT username,total_points from stuff_users ORDER BY total_points DESC;"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

class LeaderboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'leaderboard'
        self.room_group_name = 'score_{}'.format(self.room_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        result = await fetchData()
        await self.send(
            text_data=json.dumps({
                "message":result
            })
        )
    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self,text_data):
        result = await fetchData()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":result
            }
        )
    async def chat_message(self,event):
        message = event.get('message')
        await self.send(
            text_data = json.dumps({
                "message":message
            })
        )    

    
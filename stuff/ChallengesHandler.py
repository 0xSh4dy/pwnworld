# Challenges Handler
from django.db import connection
from asgiref.sync import sync_to_async
from .models import Challenges,Users,Events
import jwt
from decouple import config
import json
from jwt.exceptions import InvalidSignatureError
from pprint import pprint
import datetime
jwt_secret = config("JWT_SECRET")
cursor = connection.cursor()

class ChallsHandler:
    def __init__(self,username):
        self.username = username
    @sync_to_async
    def checkFlag(self,flag,challenge_name,usr):
        try:
            username = jwt.decode(usr,jwt_secret,algorithms=["HS256"])
            username = username.get("username")
            try:
                user_obj = Users.objects.get(username=username)
                try:
                    chal_obj = Challenges.objects.get(challenge_name=challenge_name)
                    real_flag = chal_obj.flag
                    if flag==real_flag:
                        if user_obj.chals_solved_name==None:
                            user_obj.chals_solved_name = []
                            user_obj.challenges_solved = 0
                        elif chal_obj.solved_by==None:
                            chal_obj.solved_by = []
                        if challenge_name not in user_obj.chals_solved_name:
                            user_obj.chals_solved_name.append(challenge_name)
                            user_obj.challenges_solved +=1 
                            chal_obj.solves+=1
                            chal_points = chal_obj.challenge_points
                            user_obj.total_points += chal_points
                            chal_obj.solved_by.append(username)
                            chal_obj.save()
                            user_obj.save()
                            event = Events.objects.create(username=username)
                            event.timing = str(datetime.datetime.now().replace(microsecond=0))
                            event.eventData = "{} solved the challenge {}".format(username,challenge_name)
                            event.save()
                            return {"flag":"Correct flag","chal_name":challenge_name,"username":username}
                            # return "Correct flag"
                        else:
                            return "Flag for a particular challenge can be submitted only once"
                                
                    else:
                        return "Incorrect flag"    
                except Challenges.DoesNotExist:
                    return "Challenge not found"    
            except Users.DoesNotExist:
                return "Invalid user"                
        except InvalidSignatureError:
            return "Invalid auth token"        

    @sync_to_async
    def likeOrDislike(self,reaction,challenge_name,user):
        try:
            dec = jwt.decode(user,key=jwt_secret,algorithms=["HS256"])
            username = dec.get("username")
            try:
                usr_obj = Users.objects.get(username=username)
                if reaction=='like':
                    if usr_obj.liked_challenges==None:
                        usr_obj.liked_challenges=[]
                        usr_obj.liked_challenges.append(challenge_name)    
                        try:
                            chal_obj = Challenges.objects.get(challenge_name=challenge_name)
                            chal_obj.likes+=1
                            chal_obj.save()
                            usr_obj.save()
                            print("First save")
                            event = Events.objects.create(username=username)
                            event.timing = str(datetime.datetime.now().replace(microsecond=0))
                            event.eventData = "{} liked the challenge {}".format(username,challenge_name)
                            event.save()
                            return {"like":"Liked a challenge","chal_name":challenge_name,"username":username}
                        except Challenges.DoesNotExist:
                            return False
                    elif challenge_name in usr_obj.liked_challenges:
                        
                        return "Already liked"
                    else:
                        usr_obj.liked_challenges.append(challenge_name)    
                        try:
                            chal_obj = Challenges.objects.get(challenge_name=challenge_name)
                            print("name",challenge_name)
                            chal_obj.likes+=1
                            chal_obj.save()
                            usr_obj.save()
                            print("Another save")
                            event = Events.objects.create(username=username)
                            event.timing = str(datetime.datetime.now().replace(microsecond=0))
                            event.eventData = "{} liked the challenge {}".format(username,challenge_name)
                            event.save()
                            return {"like":"Liked a challenge","chal_name":challenge_name,"username":username}

                        except Challenges.DoesNotExist:
                            return False    
                elif reaction=='dislike':
                    if usr_obj.disliked_challenges==None:
                        usr_obj.disliked_challenges=[]
                        usr_obj.disliked_challenges.append(challenge_name)    
                        try:
                            chal_obj = Challenges.objects.get(challenge_name=challenge_name)
                            chal_obj.dislikes+=1
                            chal_obj.save()
                            usr_obj.save()
                            event = Events.objects.create(username=username)
                            event.timing = str(datetime.datetime.now().replace(microsecond=0))
                            event.eventData = "{} disliked the challenge {}".format(username,challenge_name)
                            event.save()
                            return {"dislike":"Disliked a challenge","chal_name":challenge_name,"username":username}
                        except Challenges.DoesNotExist:
                            return False
                    elif challenge_name in usr_obj.disliked_challenges:
                        return "Already disliked"
                    else:
                        usr_obj.disliked_challenges.append(challenge_name)    
                        try:
                            chal_obj = Challenges.objects.get(challenge_name=challenge_name)
                            chal_obj.dislikes+=1
                            chal_obj.save()
                            usr_obj.save()
                            event = Events.objects.create(username=username)
                            event.timing = str(datetime.datetime.now().replace(microsecond=0))
                            event.eventData = "{} disliked the challenge {}".format(username,challenge_name)
                            event.save()
                            return {"dislike":"Disliked a challenge","chal_name":challenge_name,"username":username}
                        except Challenges.DoesNotExist:
                            return False   
                else:
                    return False
            except Users.DoesNotExist:
                return False    
            
        except InvalidSignatureError:
            return 'Invalid auth token'

        
    @sync_to_async        
    def comment(self,comment,challenge_name,user):
        try:
            chal_obj = Challenges.objects.get(challenge_name=challenge_name)
            comment = json.loads(comment)
            chal_obj.comments.append(comment)
            # chal_obj.save()
            return True
        except Challenges.DoesNotExist:
            return False    
    @sync_to_async        
    def filter(self,filter,user):
        try:
            if filter=="solves":
                query = "SELECT * FROM stuff_challenges ORDER BY solves DESC;"
            elif filter=="points":
                query = "SELECT * FROM stuff_challenges ORDER BY challenge_points;"
            elif filter=="likes":
                query = "SELECT * FROM stuff_challenges ORDER BY likes DESC;"    
            cursor.execute(query)
            result = cursor.fetchall()
            res = []
            for r in result:
                li = list(r)
                li.pop(8)
                res.append(li)
            return res
        except Exception:
            return False
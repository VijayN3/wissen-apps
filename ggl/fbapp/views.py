from django.http import HttpResponse
import facebook
import json
import logging
import time
from key import missing_key
#import del1
from fbapp.models import UserProfile
from fbapp.models import ids
#from fbapp.models import user_groups
from fbapp.models import user_likes
from fbapp.models import user_educations
from fbapp.models import friends_interest
#from fbapp.models import friends_location
logger = logging.getLogger("projectx.log")
def index(request,ACCESS_TOKEN):
    if(ACCESS_TOKEN):
      logger.info(ACCESS_TOKEN)
      g=facebook.GraphAPI(ACCESS_TOKEN)
      user_profile=g.get_object('me')
      user_friends=g.get_connections('me','friends')
      logger.info(user_profile)
      a=user_profile.keys()
      logger.info(a) 
      try:
       missing_key(a,user_profile)
#---------storing user profile in database---------
       p1=UserProfile(UserId=user_profile['id'],RelationStatus=user_profile['relationship_status'],FirstName=user_profile['first_name'],LastName=user_profile['last_name'],Name=user_profile['name'],Gender=user_profile['gender'],
Religion=user_profile['religion'],Birthday=user_profile['birthday'],CurrentLoc=user_profile['location']['name'],HomeTown=user_profile['hometown']['name'],email=user_profile['email'])
       p1.save(using='facebook')
#--------storing user friends profile in database:
       len_usr_frn=len(user_friends['data'])
       for i in range(1):
         user_frnds_dtls=user_friends['data'][i]['id']  
         user_friends_profile=g.get_object(user_frnds_dtls)
         b=user_friends_profile.keys()
         missing_key(b,user_friends_profile)
         p2=UserProfile(UserId=user_friends_profile['id'],RelationStatus=user_friends_profile['relationship_status'],FirstName=user_friends_profile['first_name'],LastName=user_friends_profile['last_name'],Name=user_friends_profile['name'],Gender=user_friends_profile['gender'],Religion=user_friends_profile['religion'],Birthday=user_friends_profile['birthday'],CurrentLoc=user_friends_profile['location']['name'],HomeTown=user_friends_profile['hometown']['name'],email=user_friends_profile['email'])
         p2.save(using='facebook')
#---------storing User Likes in Database:
       user_like=g.get_connections('me','likes')
       likes_key=user_like.keys()
       len_likes=len(user_like['data'])
       for i in range(len_likes):
        p3=user_likes(user_id=user_profile['id'],likes_id=user_like['data'][i]['id'],likes_category=user_like['data'][i]['category'],likes_name=user_like['data'][i]['name'])
        p3.save(using='facebook')
#------mappinf of ids in Database:
       p4=ids(userid=user_profile['id'],friendsid=user_friends_profile['id'])
       p4.save(using='facebook')
#------storing User Education in Database:
       len_edu=len(user_profile['education'])
       for i in range(len_edu):
         school_id=user_profile['education'][i]['school']['id']
         school_name=user_profile['education'][i]['school']['name']
         school_type=user_profile['education'][i]['type']
         p5=user_educations(user_id=user_profile['id'],school_id=user_profile['education'][i]['school']['id'],school_name=user_profile['education'][i]['school']['name'],school_type=user_profile['education'][i]['type'])
         p5.save(using='facebook')
      except ValueError:
       return HttpResponse("sorry")




import time, datetime
from decimal import Decimal

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.query_utils import Q

from facebook import GraphAPI

time_format = "%Y-%m-%dT%H:%M:%S+0000"
# 2011-06-13T19:05:38+0000

FACEBOOK_PERMISSIONS = 'email,read_stream,publish_stream,offline_access,user_photos,friends_photos'

USER_PASSWORD = 'password'

class FbModel():

    @staticmethod    
    def rekey(f):
        d = {}
        for k in f.keys():
            v = f[k]
            k = str(k)
            d[k] = v 
        return d
    
    @staticmethod
    def parse_date(v):
        d = datetime.datetime.fromtimestamp(time.mktime(time.strptime(v, time_format)))
        return d
    
class FbUser(models.Model):

    # id is facebook id    
    id = models.CharField(max_length=200,primary_key=True,null=False,blank=False)
    user = models.ForeignKey(User,null=False,blank=False)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=False,blank=False)
    pic_square = models.CharField(max_length=200)
    profile_url = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)
    birthday = models.CharField(max_length=200)
    relationship_status = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200,null=False,blank=False)
    created_time = models.DateTimeField(editable=False)
    updated_time = models.DateTimeField(editable=False,auto_now=True)

    def save(self):
        if not self.created_time:
            self.created_time = datetime.datetime.today()
        self.updated_time = datetime.datetime.today()
        super(FbUser, self).save()    

    @staticmethod
    def trans(d):
        d = FbModel.rekey(d)
        obj = FbUser(**d)
        return obj

    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.email)

    @classmethod
    def fields(cls):
        return "id,username,name,first_name,last_name,email,location,hometown,birthday,relationship_status"

    @classmethod
    def get_birthdays(cls, fbuser, date, days_advance):
        format_today = date.strftime("%B %e")
        interval = datetime.timedelta(days=days_advance)
        date_future = date + interval
        format_future = date_future.strftime("%B %e")
        friends = FbUser.objects.filter(Q(friends__id=fbuser.id), Q(birthday__startswith=format_today) | Q(birthday__startswith=format_future))
        return friends
    
    @classmethod
    def get_me(cls, user):
        me = FbUser.objects.filter(user__id=user.id)
        if (len(me) == 1):
            return me[0]
        else:
            raise Exception("no FbUser for logged in User")

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    
    fb_user = models.ForeignKey(FbUser,editable=False,null=False,blank=False)
    fb_post_default = models.BooleanField()
    
    last_login_time = models.DateTimeField(editable=False,null=True,blank=True)
    last_processed_time = models.DateTimeField(editable=False,null=True,blank=True)

    deleted = models.BooleanField()
    created_by = models.ForeignKey(User,null=False,blank=False, related_name='+')
    created_time = models.DateTimeField(editable=False)
    updated_by = models.ForeignKey(User,null=False,blank=False, related_name='+')
    updated_time = models.DateTimeField(editable=False,auto_now=True)

    def url(self):
        return UserProfile.get_url(self.user.id)
    
    @staticmethod
    def get_url(id):
        url = settings.WEB_PATH + "/profile/" 
        url = url + str(id)
        return url
        
    def name(self):
        if (self.fb_user):
            return self.fb_user.name
        else:
            return self.user.name

    def fb_image_url(self):
        url = "https://graph.facebook.com/me/picture?access_token=%s" % (self.fb_user.access_token)
        return url

    def save(self):
        if not self.created_time:
            self.created_time = datetime.datetime.today()
        self.updated_time = datetime.datetime.today()
        super(UserProfile, self).save()    
        
    @staticmethod
    def get_or_make_profile(user):
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            profile = UserProfile()
            profile.user = user
            profile.created_by = user
            profile.updated_by = user
        return profile       

class Beta(models.Model):
    email = models.CharField(max_length=200)
    android = models.BooleanField()
    iphone = models.BooleanField()

def get_graph(access_token):
    graph = False
    if access_token:
        graph = GraphAPI(access_token)
    return graph
    

    
    



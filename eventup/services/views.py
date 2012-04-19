# Python
import oauth2 as oauth
from oauth2 import *
import cgi
import urllib

# Django
from django.shortcuts import *
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from services.models import *
from django.template.context import RequestContext
from home.utils import *

MOBILE_SUCCESS_REDIRECT = "emoto://success"
LOGIN_LANDING_URL = '/home'

FACEBOOK_AUTHORIZE_URL = 'https://www.facebook.com/dialog/oauth'
FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'

def common_login (request):
    
    login_url = None
    if (is_iphone_app(request)):
        login_url = "/mobile/login"
    else:
        login_url = "/facebook/login"
    
    context = make_context(request, {'user':request.user, 'login_url':login_url})
    return render_to_response('login.html', context, context_instance=RequestContext(request))

def common_logout (request):
    
    from django.contrib.auth import logout
    logout (request)
    
    return HttpResponseRedirect('/home')

def facebook_login(request):

    auth_url = settings.WEB_PATH + "/facebook/login/auth"    
    url = "%s?client_id=%s&redirect_uri=%s&scope=%s" % (FACEBOOK_AUTHORIZE_URL, settings.FB_APP, auth_url, FACEBOOK_PERMISSIONS)
    
    return HttpResponseRedirect(url)
    
def facebook_auth(request, auth_redirect_url=None, success_redirect_url=None):

    is_not_logged_in = request.user.is_anonymous()

    code = request.GET["code"]

    if (not auth_redirect_url):
        auth_redirect_url = settings.WEB_PATH + "/facebook/login/auth"    
    url = "%s?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s" % (FACEBOOK_ACCESS_TOKEN_URL, settings.FB_APP, auth_redirect_url, settings.FB_SECRET, code)
    
    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()
    parts = html.split('&')
    access_token = parts[0].split('=')[1]

    success = process_token(request, access_token, is_not_logged_in)
    
    if (success):
        if (not success_redirect_url):
            success_redirect_url = LOGIN_LANDING_URL
        return redirect(success_redirect_url)
    else:
        pass

def mobile (request):
    
    required_login = request.GET.get("forced", None)
    if request.user.is_authenticated() and not required_login:
         return redirect(MOBILE_SUCCESS_REDIRECT)   
    else:
        return common_login(request);
    
def mobile_login(request):

    auth_url = settings.WEB_PATH + "/mobile/login/auth"    
    url = "%s?client_id=%s&redirect_uri=%s&scope=%s&display=wap" % (FACEBOOK_AUTHORIZE_URL, settings.FB_APP, auth_url, FACEBOOK_PERMISSIONS)
    
    return HttpResponseRedirect(url)
    
def mobile_auth(request):

    auth_redirect_url = settings.WEB_PATH + "/mobile/login/auth" 
    success_redirect_url = MOBILE_SUCCESS_REDIRECT
    return facebook_auth(request, auth_redirect_url, success_redirect_url)

def process_token (request, access_token, is_not_logged_in):
    
    # get facebook user
    fbuser = get_fbuser(access_token)
    
    if (fbuser):

        email = fbuser.email

        # if no user, create it
        try:
            # BUGBUG: fails b/c username for twitter is totally different than username for facebook!
            user = User.objects.get(username=email)
            print "find user", user

        except User.DoesNotExist:

            user = User.objects.create_user(email, email, USER_PASSWORD)
            print "create user", user
            user.first_name = fbuser.first_name
            user.last_name = fbuser.last_name
            res = user.save()
            print "save user", res

        # save user/token to facebook
        fbuser.access_token = access_token
        fbuser.user = user
        res = fbuser.save()
        print "save user token", fbuser, ":", res

        profile = UserProfile.get_or_make_profile(user)
        profile.fb_user = fbuser
        res = profile.save()
        print "save user profile", profile, ":", res

        # log in
        if (is_not_logged_in):
            user = authenticate(username=email, password=USER_PASSWORD)
            print "authenticate user", user
            res  = login(request, user)
            print "login user", res
        
        return True
    
    return False

def get_fbuser(access_token):
    
    print "access_token", access_token
    if (access_token):
        graph = get_graph(access_token)
        print "graph", graph
        if (graph):
            user = graph.get_object("me", fields=FbUser.fields())

    print "user", user
    if (user):
        user = FbUser.trans(user)

#    user = FbUser.objects.get(id='100002040217300')
    return user

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
from django.utils import simplejson

from services.models import *
from django.template.context import RequestContext
from home.utils import *

def home (request):
    
    if request.user.is_authenticated():
        #return picks(request)	
 		context = make_context(request, {})
 		return render_to_response('home.html', context, context_instance=RequestContext(request))
    else:
		context = make_context(request, {})
 		return render_to_response('home.html', context, context_instance=RequestContext(request))
        #return splash(request)

def splash(request):
    context = make_context(request, {})
    return render_to_response('splash.html', context, context_instance=RequestContext(request))

def about (request):
    
    context = make_context(request, {})
    return render_to_response('about.html', context, context_instance=RequestContext(request))

def help (request):
    
    context = make_context(request, {})
    return render_to_response('help.html', context, context_instance=RequestContext(request))

newsletters = [
    {
        'id': 0,
        'customer': 'Will'
    }
]

items = [
	[
    {
        'id': 0,
        'parent_id': 0,
        'name': 'GoRide lets you stay connected on your ride!',
        'description': 'Go hands free on your next 50-miler, make calls, find the next restroom, and (for the brave) check e-mail. Compatibile with iPhone.',
        'img': '/static/img/test1/Bike.jpg',
        'price': 30,
        'discount': 10,
		'sd':'GoRide lets you stay connected on your ride!',
		'main':'Set the trend this season with GoRide, District Threads and other great finds!'
    },
    {
        'id': 1,
        'parent_id': 0,
        'name': 'Zaazle Black Diamond Tee',
        'description': 'Stay comfortable when you tear down that Black Diamond. Double-needle stitch at the bottom and sleeve hems for extra durability.',
        'img': '/static/img/test1/T shirt 2.jpg',
        'price': 16,
        'discount': 15,
    },
    {
        'id': 2,
        'parent_id': 0,
        'name': 'Pyle Pro Ski Watch',
        'description': 'Perfect on the slopes. Stores skiing data, including altitude, ski slope, speed of descent, and time elapsed. Heck, it can even predict the weather!',
        'img': '/static/img/test1/watch.jpg',
        'price': 75,
        'discount': 15,
    },
    {
        'id': 3,
        'parent_id': 0,
        'name': 'District Threads Cap',
        'description': 'Enzyme-washed baseball hat that oozes attitude. Comfortable as an old friend, it\'s 100% cotton.',
        'img': '/static/img/test1/Hat.jpg',
        'price': 25,
        'discount': 10,
    },
    {
        'id': 4,
        'parent_id': 0,
        'name': 'Columbia Fast Trek II Fleece Jacket',
        'description': 'Enjoy you jog or hike with this versatile & stylish fleece over a technical tee or underneath your favorite shell.',
        'img': '/static/img/test1/Fleece.jpg',
        'price': 27,
        'discount': 32,
    },
    {
        'id': 5,
        'parent_id': 0,
        'name': 'Barn Burner Arnette Sunglasses',
        'description': 'The Barn Burner provides maximum protection and coverage, whether you\'re riding your moto or just hanging at a BBQ. Comfortable frames and lightweight lenses mean you\'ll probably forget you\'re even wearing them!',
        'img': '/static/img/test1/glasses.jpg',
        'price': 64,
        'discount': 20,
    },
    {
        'id': 6,
        'parent_id': 0,
        'name': 'Hanes Double Pocket Polo',
        'description': 'The polo rethought, for a look that\'s decidedly more retro. Super comfortable Soft cotton-poly blend.',
        'img': '/static/img/test1/shirt.jpg',
        'price': 30,
        'discount': 50,
    }],
###another user
	[
    {
        'id': 0,
        'parent_id': 1,
        'name': 'Awesome Bike!',
        'description': 'Go hands free on your next 50-miler, make calls, find the next restroom, and (for the brave) check e-mail. Compatibile with iPhone.',
        'img': '/static/img/test2/bengals.jpg',
        'price': 30,
        'discount': 10,
		'sd':'Awesome Bangals!',
		'main':'Set the trend this season with bengals,dresses and the bag of your dreams !'
    },
    {
        'id': 1,
        'parent_id': 1,
        'name': 'Awesome Diamond Tee',
        'description': 'Stay comfortable when you tear down that Black Diamond. Double-needle stitch at the bottom and sleeve hems for extra durability.',
        'img': '/static/img/test2/T shirt 2.jpg',
        'price': 16,
        'discount': 15,
    },
    {
        'id': 2,
        'parent_id': 1,
        'name': 'Awesome Ski Watch',
        'description': 'Perfect on the slopes. Stores skiing data, including altitude, ski slope, speed of descent, and time elapsed. Heck, it can even predict the weather!',
        'img': '/static/img/test2/watch.jpg',
        'price': 75,
        'discount': 15,
    },
    {
        'id': 3,
        'parent_id': 1,
        'name': 'Awesome Threads Cap',
        'description': 'Enzyme-washed baseball hat that oozes attitude. Comfortable as an old friend, it\'s 100% cotton.',
        'img': '/static/img/test2/Hat.jpg',
        'price': 25,
        'discount': 10,
    },
    {
        'id': 4,
        'parent_id': 1,
        'name': 'Awesome Fleece Jacket',
        'description': 'Enjoy you jog or hike with this versatile & stylish fleece over a technical tee or underneath your favorite shell.',
        'img': '/static/img/test2/Fleece.jpg',
        'price': 27,
        'discount': 32,
    },
    {
        'id': 5,
        'parent_id': 1,
        'name': 'Fat Sunglasses',
        'description': 'The Barn Burner provides maximum protection and coverage, whether you\'re riding your moto or just hanging at a BBQ. Comfortable frames and lightweight lenses mean you\'ll probably forget you\'re even wearing them!',
        'img': '/static/img/test2/glasses.jpg',
        'price': 64,
        'discount': 20,
    },
    {
        'id': 6,
        'parent_id': 1,
        'name': 'Solo Polo',
        'description': 'The polo rethought, for a look that\'s decidedly more retro. Super comfortable Soft cotton-poly blend.',
        'img': '/static/img/test2/shirt.jpg',
        'price': 30,
        'discount': 50,
    }]

]



def picks(request,user=0):
#context = make_context(request, {'items': items[int(user)]})
    context = make_context(request, {'items': items[int(user)]})
    return render_to_response('picks.html', context, context_instance=RequestContext(request))


         
def pick(request, user=0, id=0):
    item = items[int(user)][int(id)];
    context = make_context(request, {'item': item, 'items': items[int(user)]})
    return render_to_response('pick.html', context, context_instance=RequestContext(request))

def buy(request, user=0, id=0):
    item = items[int(user)][int(id)];

    context = make_context(request, {'item': item})
    return render_to_response('buy.html', context, context_instance=RequestContext(request))

@login_required
def profile (request):
    
    context = make_context(request, {})
    return render_to_response('profile.html', context, context_instance=RequestContext(request))

@login_required
def tools (request):

    context = make_context(request, {})
    return render_to_response('tools.html', context, context_instance=RequestContext(request))

def test (request):
    to_json = {
        "key1": "value1",
        "key2": "value2"
    }
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

@login_required
def profile_albums (request):

    user = request.user
    profile = user.get_profile()
    graph = get_graph(profile.fb_user.access_token)
    albums = graph.get_albums("me")
    print albums
    
    context = make_context(request, {'albums':albums})
    return render_to_response('albums.html', context, context_instance=RequestContext(request))


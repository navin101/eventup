from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # non-authenticated
    url(r'^$', 'home.views.home'),
    url(r'^home$', 'home.views.home'),
    url(r'^about', 'home.views.about'),
    url(r'^help', 'home.views.help'),
    url(r'^splash$', 'home.views.splash'),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),

    # auth code
    url(r'^login$', 'services.views.common_login'),
    url(r'^logout$', 'services.views.common_logout'),
    url(r'^facebook/login/?$', 'services.views.facebook_login'),
    url(r'^facebook/login/auth/?$', 'services.views.facebook_auth'),
    url(r'^facebook/logout/?$', 'services.views.facebook_login'),

    # products
    url(r'^picks/(\d+)?$', 'home.views.picks'),
    url(r'^pick/(\d+)/(\d+)?$', 'home.views.pick'),
    url(r'^buy/(\d+)/(\d+)?$', 'home.views.buy'),

    # profile & settings
    url(r'^profile/albums$', 'home.views.profile_albums'),
    url(r'^profile$', 'home.views.profile'),
    
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tools', 'home.views.tools'),
    url(r'^test$', 'home.views.test'),
)

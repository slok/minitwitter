from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tl/', include('timeline.urls')),
    url(r'^api/{0}/'.format(settings.API_VERSION), include('api.urls')),
    # Examples:
    # url(r'^$', 'minitwitter.views.home', name='home'),
    # url(r'^minitwitter/', include('minitwitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

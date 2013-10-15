from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
    url(r'messages/$',
        views.MessageList.as_view(),
        name='message-list'),

    url(r'messages/(?P<pk>[0-9]+)/$',
        views.MessageDetail.as_view(),
        name='message-detail'),

    url(r'users/$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns = format_suffix_patterns(urlpatterns)
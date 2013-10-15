from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
    url(r'messages$', views.MessageList.as_view()),
    url(r'messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
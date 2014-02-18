import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

from movies.views import load

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<addr>.*)$', load, {}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)

from django.conf.urls.defaults import *

urlpatterns = patterns('wolves.views',
    url(r'^ping$', 'ping', name='wolves_ping'),
)

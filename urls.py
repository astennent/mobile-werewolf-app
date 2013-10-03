from django.conf.urls.defaults import *

urlpatterns = patterns('wolves.views',
    url(r'^ping$', 'ping'),
    url(r'^create_account$', 'create_account'),
    url(r'^delete_account$', 'delete_account'),
  
)

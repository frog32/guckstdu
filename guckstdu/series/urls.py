from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^top/$', 'series.views.top_series', name='top_series'),
)

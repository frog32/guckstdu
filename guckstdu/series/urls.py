from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^top/$', 'series.views.top_series', name='top_series'),
    url(r'^series/$', 'series.views.series_details', name='series_details'),
    url(r'^season/$', 'series.views.season_details', name='season_details'),
    url(r'^episode/$', 'series.views.episode_details', name='episode_details'),
)

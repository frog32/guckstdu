import os
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.start', name='start'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^series/', include('series.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), 'media/')}),
)

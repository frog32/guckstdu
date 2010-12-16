from series.models import Series, Season, Episode

from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 0

class SeasonAdmin(admin.ModelAdmin):
    inlines = (EpisodeInline,)
    list_display = ('__unicode__', 'episode_count')
    # list_filter = ('series',)

    def changelist_view(self, *args, **kwargs):
        return super(SeasonAdmin, self).changelist_view(*args, **kwargs)

class SeasonInline(admin.TabularInline):
    model = Season

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    
    def get_urls(self):
        urlpatterns = super(SeriesAdmin, self).get_urls()
        season_admin = SeasonAdmin(Season,self.admin_site)
        extra_urlpatterns = patterns('',
                            url(r'^(.+)/season/',include(season_admin.urls)),
                        )
        return extra_urlpatterns + urlpatterns
    
    
admin.site.register(Series, SeriesAdmin)
admin.site.register(Season, SeasonAdmin)

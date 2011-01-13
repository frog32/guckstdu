from django.db import models
from django.contrib.auth.models import User

class SeriesManager(models.Manager):
    """
    Manager for the series model
    """
    def top_10(self):
        return self.annotate(models.Count('fans')).order_by('-fans__count')

class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fans = models.ManyToManyField(User, related_name = 'favourite_series', blank=True)
	
    objects = SeriesManager()
	
    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Serien"
    
    def __unicode__(self):
        return self.name

        
class Season(models.Model):
    series = models.ForeignKey(Series, related_name="seasons")
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    
    class Meta:
        verbose_name = "Staffel"
        verbose_name_plural = "Staffeln"
    
    def __unicode__(self):
        return '%s Staffel %d' % (self.series.name, self.number)

    def episode_count(self):
        return self.episodes.count()
    episode_count.description = "Anzahl Episoden"
        
class Episode(models.Model):
	season = models.ForeignKey(Season, related_name="episodes")
	number = models.IntegerField()
	name = models.CharField(max_length=100)
	duration = models.IntegerField()
	
	class Meta:
		verbose_name = "Episode"
		verbose_name_plural = "Episoden"
		
	def __unicode__(self):
		return '%s Episode %d' % (self.season.__unicode__(), self.number)
        
class Station(models.Model):
	name = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = "Sender"
		verbose_name_plural = "Sender"
	
	def __unicode__(self):
		return self.name
		
class Runtime(models.Model):
	episode = models.ForeignKey(Episode, related_name="runtimes")
	language = models.CharField(max_length=5)
	station = models.ForeignKey(Station, related_name="program")
	datetime = models.DateTimeField()
	
	class Meta:
		verbose_name = "Sendezeit"
		verbose_name_plural = "Sendezeiten"
		
	def __unicode__(self):
		return self.episode.season.series.name + ' s' + str(self.episode.season.number) + 'e' + str(self.episode.number)
	

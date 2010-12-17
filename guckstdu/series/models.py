from django.db import models

class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
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

class Runtime(models.Model):
    episode = models.ForeignKey(Episode, related_name="runtimes")
    language = models.CharField(max_length=5)
    station = models.ForeignKey(Station, related_name="program")
    datetime = models.DateTimeField()
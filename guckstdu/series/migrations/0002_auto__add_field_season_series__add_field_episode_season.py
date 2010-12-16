# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Season.series'
        db.add_column('series_season', 'series', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='seasons', to=orm['series.Series']), keep_default=False)

        # Adding field 'Episode.season'
        db.add_column('series_episode', 'season', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='episodes', to=orm['series.Season']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Season.series'
        db.delete_column('series_season', 'series_id')

        # Deleting field 'Episode.season'
        db.delete_column('series_episode', 'season_id')


    models = {
        'series.episode': {
            'Meta': {'object_name': 'Episode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': "orm['series.Season']"})
        },
        'series.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seasons'", 'to': "orm['series.Series']"})
        },
        'series.series': {
            'Meta': {'object_name': 'Series'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['series']

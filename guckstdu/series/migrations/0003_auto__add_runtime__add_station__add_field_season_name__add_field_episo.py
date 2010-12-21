# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Runtime'
        db.create_table('series_runtime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(related_name='runtimes', to=orm['series.Episode'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(related_name='program', to=orm['series.Station'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('series', ['Runtime'])

        # Adding model 'Station'
        db.create_table('series_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('series', ['Station'])

        # Adding field 'Season.name'
        db.add_column('series_season', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Episode.duration'
        db.add_column('series_episode', 'duration', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Runtime'
        db.delete_table('series_runtime')

        # Deleting model 'Station'
        db.delete_table('series_station')

        # Deleting field 'Season.name'
        db.delete_column('series_season', 'name')

        # Deleting field 'Episode.duration'
        db.delete_column('series_episode', 'duration')


    models = {
        'series.episode': {
            'Meta': {'object_name': 'Episode'},
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': "orm['series.Season']"})
        },
        'series.runtime': {
            'Meta': {'object_name': 'Runtime'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'runtimes'", 'to': "orm['series.Episode']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'program'", 'to': "orm['series.Station']"})
        },
        'series.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seasons'", 'to': "orm['series.Series']"})
        },
        'series.series': {
            'Meta': {'object_name': 'Series'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'series.station': {
            'Meta': {'object_name': 'Station'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['series']

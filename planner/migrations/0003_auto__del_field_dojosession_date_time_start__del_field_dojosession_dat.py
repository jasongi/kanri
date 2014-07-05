# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DojoSession.date_time_start'
        db.delete_column(u'planner_dojosession', 'date_time_start')

        # Deleting field 'DojoSession.date_time_end'
        db.delete_column(u'planner_dojosession', 'date_time_end')

        # Adding field 'DojoSession.date'
        db.add_column(u'planner_dojosession', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'DojoSession.start'
        db.add_column(u'planner_dojosession', 'start',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2014, 7, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'DojoSession.end'
        db.add_column(u'planner_dojosession', 'end',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2014, 7, 5, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'DojoSession.date_time_start'
        raise RuntimeError("Cannot reverse this migration. 'DojoSession.date_time_start' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'DojoSession.date_time_start'
        db.add_column(u'planner_dojosession', 'date_time_start',
                      self.gf('django.db.models.fields.DateTimeField')(unique=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'DojoSession.date_time_end'
        raise RuntimeError("Cannot reverse this migration. 'DojoSession.date_time_end' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'DojoSession.date_time_end'
        db.add_column(u'planner_dojosession', 'date_time_end',
                      self.gf('django.db.models.fields.DateTimeField')(unique=True),
                      keep_default=False)

        # Deleting field 'DojoSession.date'
        db.delete_column(u'planner_dojosession', 'date')

        # Deleting field 'DojoSession.start'
        db.delete_column(u'planner_dojosession', 'start')

        # Deleting field 'DojoSession.end'
        db.delete_column(u'planner_dojosession', 'end')


    models = {
        u'planner.dojosession': {
            'Meta': {'object_name': 'DojoSession'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['planner.DojoTerm']"})
        },
        u'planner.dojoterm': {
            'Meta': {'object_name': 'DojoTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['planner']
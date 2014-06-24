# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DojoSession.date_time'
        db.delete_column(u'planner_dojosession', 'date_time')

        # Adding field 'DojoSession.date_time_start'
        db.add_column(u'planner_dojosession', 'date_time_start',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 21, 0, 0), unique=True),
                      keep_default=False)

        # Adding field 'DojoSession.date_time_end'
        db.add_column(u'planner_dojosession', 'date_time_end',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 21, 0, 0), unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DojoSession.date_time'
        db.add_column(u'planner_dojosession', 'date_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 21, 0, 0), unique=True),
                      keep_default=False)

        # Deleting field 'DojoSession.date_time_start'
        db.delete_column(u'planner_dojosession', 'date_time_start')

        # Deleting field 'DojoSession.date_time_end'
        db.delete_column(u'planner_dojosession', 'date_time_end')


    models = {
        u'planner.dojosession': {
            'Meta': {'object_name': 'DojoSession'},
            'date_time_end': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'}),
            'date_time_start': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['planner.DojoTerm']"})
        },
        u'planner.dojoterm': {
            'Meta': {'object_name': 'DojoTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['planner']
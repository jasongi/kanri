# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DojoSession.current'
        db.delete_column(u'planner_dojosession', 'current')


    def backwards(self, orm):
        # Adding field 'DojoSession.current'
        db.add_column(u'planner_dojosession', 'current',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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
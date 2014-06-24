# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DojoTerm'
        db.create_table(u'planner_dojoterm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'planner', ['DojoTerm'])

        # Adding model 'DojoSession'
        db.create_table(u'planner_dojosession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['planner.DojoTerm'])),
            ('date_time_start', self.gf('django.db.models.fields.DateTimeField')(unique=True)),
            ('date_time_end', self.gf('django.db.models.fields.DateTimeField')(unique=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'planner', ['DojoSession'])


    def backwards(self, orm):
        # Deleting model 'DojoTerm'
        db.delete_table(u'planner_dojoterm')

        # Deleting model 'DojoSession'
        db.delete_table(u'planner_dojosession')


    models = {
        u'planner.dojosession': {
            'Meta': {'object_name': 'DojoSession'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
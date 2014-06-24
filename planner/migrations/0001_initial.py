# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dojo'
        db.create_table(u'planner_dojo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(unique=True)),
        ))
        db.send_create_signal(u'planner', ['Dojo'])


    def backwards(self, orm):
        # Deleting model 'Dojo'
        db.delete_table(u'planner_dojo')


    models = {
        u'planner.dojo': {
            'Meta': {'object_name': 'Dojo'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['planner']
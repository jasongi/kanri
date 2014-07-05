# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ninja.gender'
        db.add_column(u'ninjas_ninja', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ninja.gender'
        db.delete_column(u'ninjas_ninja', 'gender')


    models = {
        u'ninjas.ninja': {
            'Meta': {'object_name': 'Ninja'},
            'aim': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'allergies': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'attended_workshop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'availabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['planner.DojoSession']", 'symmetrical': 'False'}),
            'black_belt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codecademy_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'general_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_experience': ('django.db.models.fields.TextField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'laptop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ninjas.Parent']"}),
            'photo_release': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'postcode': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4'}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '7'}),
            'scratch_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'})
        },
        u'ninjas.parent': {
            'Meta': {'object_name': 'Parent'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'})
        },
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

    complete_apps = ['ninjas']
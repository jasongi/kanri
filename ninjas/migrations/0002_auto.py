# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field availabilities on 'Ninja'
        m2m_table_name = db.shorten_name(u'ninjas_ninja_availabilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ninja', models.ForeignKey(orm[u'ninjas.ninja'], null=False)),
            ('dojosession', models.ForeignKey(orm[u'planner.dojosession'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ninja_id', 'dojosession_id'])


    def backwards(self, orm):
        # Removing M2M table for field availabilities on 'Ninja'
        db.delete_table(db.shorten_name(u'ninjas_ninja_availabilities'))


    models = {
        u'ninjas.ninja': {
            'Meta': {'ordering': "['name']", 'object_name': 'Ninja'},
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
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'planner.dojosession': {
            'Meta': {'object_name': 'DojoSession'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rooms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['planner.Room']", 'symmetrical': 'False', 'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['planner.DojoTerm']"})
        },
        u'planner.dojoterm': {
            'Meta': {'object_name': 'DojoTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'planner.room': {
            'Meta': {'object_name': 'Room'},
            'capacity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['ninjas']
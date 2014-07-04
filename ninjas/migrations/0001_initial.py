# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parent'
        db.create_table(u'ninjas_parent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('phone', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'ninjas', ['Parent'])

        # Adding model 'Ninja'
        db.create_table(u'ninjas_ninja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('postcode', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=4)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('school_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=7)),
            ('allergies', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('attended_workshop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referral', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('laptop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('aim', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('general_knowledge', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('scratch_knowledge', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('codecademy_knowledge', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('language_experience', self.gf('django.db.models.fields.TextField')(max_length=140, null=True, blank=True)),
            ('black_belt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('photo_release', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ninjas.Parent'])),
        ))
        db.send_create_signal(u'ninjas', ['Ninja'])

        # Adding M2M table for field availabilities on 'Ninja'
        m2m_table_name = db.shorten_name(u'ninjas_ninja_availabilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ninja', models.ForeignKey(orm[u'ninjas.ninja'], null=False)),
            ('dojosession', models.ForeignKey(orm[u'planner.dojosession'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ninja_id', 'dojosession_id'])


    def backwards(self, orm):
        # Deleting model 'Parent'
        db.delete_table(u'ninjas_parent')

        # Deleting model 'Ninja'
        db.delete_table(u'ninjas_ninja')

        # Removing M2M table for field availabilities on 'Ninja'
        db.delete_table(db.shorten_name(u'ninjas_ninja_availabilities'))


    models = {
        u'ninjas.ninja': {
            'Meta': {'object_name': 'Ninja'},
            'aim': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'allergies': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'attended_workshop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'availabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['planner.DojoSession']", 'symmetrical': 'False'}),
            'black_belt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codecademy_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
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
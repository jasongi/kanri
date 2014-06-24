# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'ninjas_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('related_ninja', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ninjas.Ninja'])),
        ))
        db.send_create_signal(u'ninjas', ['Contact'])

        # Adding model 'Ninja'
        db.create_table(u'ninjas_ninja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('school_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('attended_workshop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referral', self.gf('django.db.models.fields.CharField')(default='OT', max_length=2)),
            ('laptop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('aim', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('general_knowledge', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('scratch_knowledge', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('codecademy_knowledge', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('language_experience', self.gf('django.db.models.fields.TextField')(max_length=140, null=True, blank=True)),
            ('black_belt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('photo_release', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'ninjas', ['Ninja'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'ninjas_contact')

        # Deleting model 'Ninja'
        db.delete_table(u'ninjas_ninja')


    models = {
        u'ninjas.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'related_ninja': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ninjas.Ninja']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ninjas.ninja': {
            'Meta': {'object_name': 'Ninja'},
            'aim': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'attended_workshop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'black_belt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codecademy_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'general_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_experience': ('django.db.models.fields.TextField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'laptop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photo_release': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'referral': ('django.db.models.fields.CharField', [], {'default': "'OT'", 'max_length': '2'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'scratch_knowledge': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'})
        }
    }

    complete_apps = ['ninjas']
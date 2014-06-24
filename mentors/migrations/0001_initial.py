# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mentor'
        db.create_table(u'mentors_mentor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uni', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('student_number', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('wwcc', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('wwcc_receipt', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('first_aid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('referral', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('aim', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('coding_experience', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('children_experience', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('children_experience_freeform', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('wants_champion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wants_lead', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wants_support', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'mentors', ['Mentor'])


    def backwards(self, orm):
        # Deleting model 'Mentor'
        db.delete_table(u'mentors_mentor')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mentors.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'aim': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'children_experience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'children_experience_freeform': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'coding_experience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'first_aid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'student_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'uni': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'wants_champion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wants_lead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wants_support': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wwcc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'wwcc_receipt': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mentors']
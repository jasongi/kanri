# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Role'
        db.create_table(u'mentors_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1024)),
        ))
        db.send_create_signal(u'mentors', ['Role'])

        # Adding model 'Mentor'
        db.create_table(u'mentors_mentor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uni', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('uni_study', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('work', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('needs_shirt', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wwcc', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('wwcc_receipt', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('curtin_status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('curtin_id', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('coding_experience', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('children_experience', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'mentors', ['Mentor'])

        # Adding M2M table for field roles_desired on 'Mentor'
        m2m_table_name = db.shorten_name(u'mentors_mentor_roles_desired')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mentor', models.ForeignKey(orm[u'mentors.mentor'], null=False)),
            ('role', models.ForeignKey(orm[u'mentors.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mentor_id', 'role_id'])


    def backwards(self, orm):
        # Deleting model 'Role'
        db.delete_table(u'mentors_role')

        # Deleting model 'Mentor'
        db.delete_table(u'mentors_mentor')

        # Removing M2M table for field roles_desired on 'Mentor'
        db.delete_table(db.shorten_name(u'mentors_mentor_roles_desired'))


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
            'children_experience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'coding_experience': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'curtin_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'curtin_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_shirt': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'roles_desired': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mentors.Role']", 'symmetrical': 'False'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'uni': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'uni_study': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'wwcc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'wwcc_receipt': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'mentors.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['mentors']
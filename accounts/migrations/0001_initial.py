# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attendance'
        db.create_table(u'attendance_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dojo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['planner.DojoSession'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('added_by', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'attendance', ['Attendance'])

        # Adding M2M table for field ninja on 'Attendance'
        m2m_table_name = db.shorten_name(u'attendance_attendance_ninja')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('attendance', models.ForeignKey(orm[u'attendance.attendance'], null=False)),
            ('ninja', models.ForeignKey(orm[u'ninjas.ninja'], null=False))
        ))
        db.create_unique(m2m_table_name, ['attendance_id', 'ninja_id'])


    def backwards(self, orm):
        # Deleting model 'Attendance'
        db.delete_table(u'attendance_attendance')

        # Removing M2M table for field ninja on 'Attendance'
        db.delete_table(db.shorten_name(u'attendance_attendance_ninja'))


    models = {
        u'attendance.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'added_by': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'dojo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['planner.DojoSession']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ninja': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ninjas.Ninja']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
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
        },
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

    complete_apps = ['attendance']
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

        # Adding model 'Room'
        db.create_table(u'planner_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('capacity', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'planner', ['Room'])

        # Adding model 'DojoSession'
        db.create_table(u'planner_dojosession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['planner.DojoTerm'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'planner', ['DojoSession'])

        # Adding M2M table for field rooms on 'DojoSession'
        m2m_table_name = db.shorten_name(u'planner_dojosession_rooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dojosession', models.ForeignKey(orm[u'planner.dojosession'], null=False)),
            ('room', models.ForeignKey(orm[u'planner.room'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dojosession_id', 'room_id'])

        # Adding model 'Shift'
        db.create_table(u'planner_shift', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentors.Mentor'])),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['planner.DojoSession'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentors.Role'])),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['planner.Room'], blank=True)),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'planner', ['Shift'])


    def backwards(self, orm):
        # Deleting model 'DojoTerm'
        db.delete_table(u'planner_dojoterm')

        # Deleting model 'Room'
        db.delete_table(u'planner_room')

        # Deleting model 'DojoSession'
        db.delete_table(u'planner_dojosession')

        # Removing M2M table for field rooms on 'DojoSession'
        db.delete_table(db.shorten_name(u'planner_dojosession_rooms'))

        # Deleting model 'Shift'
        db.delete_table(u'planner_shift')


    models = {
        u'accounts.kanriuser': {
            'Meta': {'object_name': 'KanriUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mentors.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'children_experience': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'coding_experience': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'curtin_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'curtin_status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_shirt': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'roles_desired': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mentors.Role']", 'symmetrical': 'False'}),
            'shift_availabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['planner.DojoSession']", 'symmetrical': 'False'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'uni': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'uni_study': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.KanriUser']", 'unique': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'wwcc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'wwcc_receipt': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'mentors.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
        },
        u'planner.shift': {
            'Meta': {'object_name': 'Shift'},
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mentors.Mentor']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mentors.Role']"}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['planner.Room']", 'blank': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['planner.DojoSession']"}),
            'start': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['planner']
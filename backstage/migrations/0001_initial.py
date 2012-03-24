# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ticket'
        db.create_table('bsg_ticket', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('reporter', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ticket_reporter', null=True, to=orm['auth.User'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ticket_owner', null=True, to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='L', max_length=1)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('backstage', ['Ticket'])

        # Adding model 'Wiki'
        db.create_table('bsg_wiki', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('document', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('backstage', ['Wiki'])

        # Adding model 'WikiAttachmentAssign'
        db.create_table('bsg_wiki_attachment_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wiki', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backstage.Wiki'])),
            ('attachment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.WebFile'])),
            ('uploader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('backstage', ['WikiAttachmentAssign'])

        # Adding unique constraint on 'WikiAttachmentAssign', fields ['wiki', 'attachment']
        db.create_unique('bsg_wiki_attachment_assign', ['wiki_id', 'attachment_id'])

        # Adding model 'LogMessage'
        db.create_table('bsg_log_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logger_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('logged_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 3, 24, 0, 0))),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('function_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('line_number', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('backstage', ['LogMessage'])

    def backwards(self, orm):
        # Removing unique constraint on 'WikiAttachmentAssign', fields ['wiki', 'attachment']
        db.delete_unique('bsg_wiki_attachment_assign', ['wiki_id', 'attachment_id'])

        # Deleting model 'Ticket'
        db.delete_table('bsg_ticket')

        # Deleting model 'Wiki'
        db.delete_table('bsg_wiki')

        # Deleting model 'WikiAttachmentAssign'
        db.delete_table('bsg_wiki_attachment_assign')

        # Deleting model 'LogMessage'
        db.delete_table('bsg_log_message')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'backstage.logmessage': {
            'Meta': {'ordering': "['-logged_time']", 'object_name': 'LogMessage', 'db_table': "'bsg_log_message'"},
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'function_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'line_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'logged_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 24, 0, 0)'}),
            'logger_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'backstage.ticket': {
            'Meta': {'object_name': 'Ticket', 'db_table': "'bsg_ticket'"},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ticket_owner'", 'null': 'True', 'to': "orm['auth.User']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ticket_reporter'", 'null': 'True', 'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'backstage.wiki': {
            'Meta': {'object_name': 'Wiki', 'db_table': "'bsg_wiki'"},
            'attachment': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.WebFile']", 'through': "orm['backstage.WikiAttachmentAssign']", 'symmetrical': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'backstage.wikiattachmentassign': {
            'Meta': {'unique_together': "(('wiki', 'attachment'),)", 'object_name': 'WikiAttachmentAssign', 'db_table': "'bsg_wiki_attachment_assign'"},
            'attachment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.WebFile']"}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'wiki': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backstage.Wiki']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.webfile': {
            'Meta': {'object_name': 'WebFile', 'db_table': "'mva_webfile'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['backstage']
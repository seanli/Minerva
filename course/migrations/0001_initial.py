# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table('mva_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('difficulty', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('course', ['Course'])

        # Adding unique constraint on 'Course', fields ['title', 'abbrev', 'institute']
        db.create_unique('mva_course', ['title', 'abbrev', 'institute_id'])

        # Adding model 'Section'
        db.create_table('mva_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(default='T', max_length=1)),
        ))
        db.send_create_signal('course', ['Section'])

        # Adding unique constraint on 'Section', fields ['course', 'start_date', 'duration']
        db.create_unique('mva_section', ['course_id', 'start_date', 'duration'])

        # Adding model 'SectionAssign'
        db.create_table('mva_section_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_user', to=orm['auth.User'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_section', to=orm['course.Section'])),
        ))
        db.send_create_signal('course', ['SectionAssign'])

        # Adding unique constraint on 'SectionAssign', fields ['user', 'section']
        db.create_unique('mva_section_assign', ['user_id', 'section_id'])

        # Adding model 'Review'
        db.create_table('mva_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='review_person_from', to=orm['auth.User'])),
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
        ))
        db.send_create_signal('course', ['Review'])

    def backwards(self, orm):
        # Removing unique constraint on 'SectionAssign', fields ['user', 'section']
        db.delete_unique('mva_section_assign', ['user_id', 'section_id'])

        # Removing unique constraint on 'Section', fields ['course', 'start_date', 'duration']
        db.delete_unique('mva_section', ['course_id', 'start_date', 'duration'])

        # Removing unique constraint on 'Course', fields ['title', 'abbrev', 'institute']
        db.delete_unique('mva_course', ['title', 'abbrev', 'institute_id'])

        # Deleting model 'Course'
        db.delete_table('mva_course')

        # Deleting model 'Section'
        db.delete_table('mva_section')

        # Deleting model 'SectionAssign'
        db.delete_table('mva_section_assign')

        # Deleting model 'Review'
        db.delete_table('mva_review')

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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'mva_country'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.institute': {
            'Meta': {'object_name': 'Institute', 'db_table': "'mva_institute'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'province_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProvinceState']"})
        },
        'core.provincestate': {
            'Meta': {'object_name': 'ProvinceState', 'db_table': "'mva_province_state'"},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'course.course': {
            'Meta': {'unique_together': "(('title', 'abbrev', 'institute'),)", 'object_name': 'Course', 'db_table': "'mva_course'"},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'course.review': {
            'Meta': {'object_name': 'Review', 'db_table': "'mva_review'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'review_person_from'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'course.section': {
            'Meta': {'unique_together': "(('course', 'start_date', 'duration'),)", 'object_name': 'Section', 'db_table': "'mva_section'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'duration': ('django.db.models.fields.CharField', [], {'default': "'T'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['course.SectionAssign']", 'symmetrical': 'False'})
        },
        'course.sectionassign': {
            'Meta': {'unique_together': "(('user', 'section'),)", 'object_name': 'SectionAssign', 'db_table': "'mva_section_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectionassign_section'", 'to': "orm['course.Section']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectionassign_user'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['course']
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Section', fields ['course', 'first_day', 'last_day', 'instructor']
        db.delete_unique('mva_section', ['course_id', 'first_day', 'last_day', 'instructor_id'])

        # Removing unique constraint on 'Course', fields ['title', 'abbrev', 'institute']
        db.delete_unique('mva_course', ['title', 'abbrev', 'institute_id'])

        # Removing unique constraint on 'SectionAssign', fields ['user', 'section']
        db.delete_unique('mva_section_assign', ['user_id', 'section_id'])

        # Deleting model 'SectionAssign'
        db.delete_table('mva_section_assign')

        # Deleting model 'Review'
        db.delete_table('mva_review')

        # Deleting model 'Course'
        db.delete_table('mva_course')

        # Deleting model 'Section'
        db.delete_table('mva_section')


    def backwards(self, orm):
        
        # Adding model 'SectionAssign'
        db.create_table('mva_section_assign', (
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_section', to=orm['core.Section'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_user', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['SectionAssign'])

        # Adding unique constraint on 'SectionAssign', fields ['user', 'section']
        db.create_unique('mva_section_assign', ['user_id', 'section_id'])

        # Adding model 'Review'
        db.create_table('mva_review', (
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 29, 22, 56, 12, 957671))),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='review_person_from', to=orm['auth.User'])),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Review'])

        # Adding model 'Course'
        db.create_table('mva_course', (
            ('difficulty', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Course'])

        # Adding unique constraint on 'Course', fields ['title', 'abbrev', 'institute']
        db.create_unique('mva_course', ['title', 'abbrev', 'institute_id'])

        # Adding model 'Section'
        db.create_table('mva_section', (
            ('last_day', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='section_instructor', to=orm['auth.User'])),
            ('first_day', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Section'])

        # Adding unique constraint on 'Section', fields ['course', 'first_day', 'last_day', 'instructor']
        db.create_unique('mva_section', ['course_id', 'first_day', 'last_day', 'instructor_id'])


    models = {
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
        }
    }

    complete_apps = ['core']

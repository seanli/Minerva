# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SectionAssign'
        db.create_table('mva_section_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_profile', to=orm['core.Profile'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_section', to=orm['core.Section'])),
        ))
        db.send_create_signal('core', ['SectionAssign'])

        # Adding unique constraint on 'SectionAssign', fields ['profile', 'section']
        db.create_unique('mva_section_assign', ['profile_id', 'section_id'])

        # Adding model 'Course'
        db.create_table('mva_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Course'])

        # Adding unique constraint on 'Course', fields ['name', 'abbrev', 'institute']
        db.create_unique('mva_course', ['name', 'abbrev', 'institute_id'])

        # Adding model 'Section'
        db.create_table('mva_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='section_professor', to=orm['core.Profile'])),
        ))
        db.send_create_signal('core', ['Section'])

        # Adding unique constraint on 'Section', fields ['course', 'start_time', 'end_time']
        db.create_unique('mva_section', ['course_id', 'start_time', 'end_time'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Section', fields ['course', 'start_time', 'end_time']
        db.delete_unique('mva_section', ['course_id', 'start_time', 'end_time'])

        # Removing unique constraint on 'Course', fields ['name', 'abbrev', 'institute']
        db.delete_unique('mva_course', ['name', 'abbrev', 'institute_id'])

        # Removing unique constraint on 'SectionAssign', fields ['profile', 'section']
        db.delete_unique('mva_section_assign', ['profile_id', 'section_id'])

        # Deleting model 'SectionAssign'
        db.delete_table('mva_section_assign')

        # Deleting model 'Course'
        db.delete_table('mva_course')

        # Deleting model 'Section'
        db.delete_table('mva_section')


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
        'core.badge': {
            'Meta': {'object_name': 'Badge', 'db_table': "'mva_badge'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_exp': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'next_lvl': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'badge_next_lvl'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Badge']"}),
            'prev_lvl': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'badge_prev_lvl'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Badge']"}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Profile']", 'through': "orm['core.BadgeAssign']", 'symmetrical': 'False'})
        },
        'core.badgeassign': {
            'Meta': {'unique_together': "(('profile', 'badge'),)", 'object_name': 'BadgeAssign', 'db_table': "'mva_badge_assign'"},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badgeassign_badge'", 'to': "orm['core.Badge']"}),
            'exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badgeassign_profile'", 'to': "orm['core.Profile']"})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "'mva_contact'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Profile']"}),
            'province_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProvinceState']"}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'core.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'mva_country'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.course': {
            'Meta': {'unique_together': "(('name', 'abbrev', 'institute'),)", 'object_name': 'Course', 'db_table': "'mva_course'"},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.faculty': {
            'Meta': {'object_name': 'Faculty', 'db_table': "'mva_faculty'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Profile']", 'through': "orm['core.FacultyAssign']", 'symmetrical': 'False'})
        },
        'core.facultyassign': {
            'Meta': {'unique_together': "(('profile', 'faculty'),)", 'object_name': 'FacultyAssign', 'db_table': "'mva_faculty_assign'"},
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facultyassign_faculty'", 'to': "orm['core.Faculty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facultyassign_profile'", 'to': "orm['core.Profile']"})
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
        'core.profile': {
            'Meta': {'object_name': 'Profile', 'db_table': "'mva_profile'"},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'instutute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tagline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'core.provincestate': {
            'Meta': {'object_name': 'ProvinceState', 'db_table': "'mva_province_state'"},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.section': {
            'Meta': {'unique_together': "(('course', 'start_time', 'end_time'),)", 'object_name': 'Section', 'db_table': "'mva_section'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section_professor'", 'to': "orm['core.Profile']"}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Profile']", 'through': "orm['core.SectionAssign']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'core.sectionassign': {
            'Meta': {'unique_together': "(('profile', 'section'),)", 'object_name': 'SectionAssign', 'db_table': "'mva_section_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectionassign_profile'", 'to': "orm['core.Profile']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectionassign_section'", 'to': "orm['core.Section']"})
        },
        'core.specialization': {
            'Meta': {'object_name': 'Specialization', 'db_table': "'mva_specialization'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Profile']", 'through': "orm['core.SpecializationAssign']", 'symmetrical': 'False'})
        },
        'core.specializationassign': {
            'Meta': {'unique_together': "(('profile', 'specialization'),)", 'object_name': 'SpecializationAssign', 'db_table': "'mva_specialization_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specializationassign_profile'", 'to': "orm['core.Profile']"}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specializationassign_specialization'", 'to': "orm['core.Specialization']"})
        }
    }

    complete_apps = ['core']

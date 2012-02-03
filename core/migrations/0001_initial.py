# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('mva_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Country'])

        # Adding model 'ProvinceState'
        db.create_table('mva_province_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Country'])),
        ))
        db.send_create_signal('core', ['ProvinceState'])

        # Adding model 'Institute'
        db.create_table('mva_institute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProvinceState'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Institute'])

        # Adding model 'Profile'
        db.create_table('mva_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tagline', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'], null=True, blank=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('influence', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Profile'])

        # Adding model 'Faculty'
        db.create_table('mva_faculty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Faculty'])

        # Adding model 'FacultyAssign'
        db.create_table('mva_faculty_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='facultyassign_profile', to=orm['core.Profile'])),
            ('faculty', self.gf('django.db.models.fields.related.ForeignKey')(related_name='facultyassign_faculty', to=orm['core.Faculty'])),
        ))
        db.send_create_signal('core', ['FacultyAssign'])

        # Adding unique constraint on 'FacultyAssign', fields ['profile', 'faculty']
        db.create_unique('mva_faculty_assign', ['profile_id', 'faculty_id'])

        # Adding model 'Specialization'
        db.create_table('mva_specialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Specialization'])

        # Adding model 'SpecializationAssign'
        db.create_table('mva_specialization_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_profile', to=orm['core.Profile'])),
            ('specialization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_specialization', to=orm['core.Specialization'])),
        ))
        db.send_create_signal('core', ['SpecializationAssign'])

        # Adding unique constraint on 'SpecializationAssign', fields ['profile', 'specialization']
        db.create_unique('mva_specialization_assign', ['profile_id', 'specialization_id'])

        # Adding model 'Contact'
        db.create_table('mva_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProvinceState'])),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Contact'])

        # Adding model 'Badge'
        db.create_table('mva_badge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('prev_lvl', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='badge_prev_lvl', unique=True, null=True, to=orm['core.Badge'])),
            ('next_exp', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('next_lvl', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='badge_next_lvl', unique=True, null=True, to=orm['core.Badge'])),
        ))
        db.send_create_signal('core', ['Badge'])

        # Adding model 'BadgeAssign'
        db.create_table('mva_badge_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_profile', to=orm['core.Profile'])),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_badge', to=orm['core.Badge'])),
            ('exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['BadgeAssign'])

        # Adding unique constraint on 'BadgeAssign', fields ['profile', 'badge']
        db.create_unique('mva_badge_assign', ['profile_id', 'badge_id'])

        # Adding model 'Course'
        db.create_table('mva_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('difficulty', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Course'])

        # Adding unique constraint on 'Course', fields ['name', 'abbrev', 'institute']
        db.create_unique('mva_course', ['name', 'abbrev', 'institute_id'])

        # Adding model 'Section'
        db.create_table('mva_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='section_instructor', to=orm['core.Profile'])),
        ))
        db.send_create_signal('core', ['Section'])

        # Adding unique constraint on 'Section', fields ['course', 'start_time', 'end_time']
        db.create_unique('mva_section', ['course_id', 'start_time', 'end_time'])

        # Adding model 'SectionAssign'
        db.create_table('mva_section_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_profile', to=orm['core.Profile'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sectionassign_section', to=orm['core.Section'])),
        ))
        db.send_create_signal('core', ['SectionAssign'])

        # Adding unique constraint on 'SectionAssign', fields ['profile', 'section']
        db.create_unique('mva_section_assign', ['profile_id', 'section_id'])

        # Adding model 'Encouragement'
        db.create_table('mva_encouragement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_to', to=orm['core.Profile'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_from', to=orm['core.Profile'])),
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 3, 16, 55, 16, 14708))),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Encouragement'])

        # Adding model 'Review'
        db.create_table('mva_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='review_person_from', to=orm['core.Profile'])),
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 3, 16, 55, 16, 15327))),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Review'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'SectionAssign', fields ['profile', 'section']
        db.delete_unique('mva_section_assign', ['profile_id', 'section_id'])

        # Removing unique constraint on 'Section', fields ['course', 'start_time', 'end_time']
        db.delete_unique('mva_section', ['course_id', 'start_time', 'end_time'])

        # Removing unique constraint on 'Course', fields ['name', 'abbrev', 'institute']
        db.delete_unique('mva_course', ['name', 'abbrev', 'institute_id'])

        # Removing unique constraint on 'BadgeAssign', fields ['profile', 'badge']
        db.delete_unique('mva_badge_assign', ['profile_id', 'badge_id'])

        # Removing unique constraint on 'SpecializationAssign', fields ['profile', 'specialization']
        db.delete_unique('mva_specialization_assign', ['profile_id', 'specialization_id'])

        # Removing unique constraint on 'FacultyAssign', fields ['profile', 'faculty']
        db.delete_unique('mva_faculty_assign', ['profile_id', 'faculty_id'])

        # Deleting model 'Country'
        db.delete_table('mva_country')

        # Deleting model 'ProvinceState'
        db.delete_table('mva_province_state')

        # Deleting model 'Institute'
        db.delete_table('mva_institute')

        # Deleting model 'Profile'
        db.delete_table('mva_profile')

        # Deleting model 'Faculty'
        db.delete_table('mva_faculty')

        # Deleting model 'FacultyAssign'
        db.delete_table('mva_faculty_assign')

        # Deleting model 'Specialization'
        db.delete_table('mva_specialization')

        # Deleting model 'SpecializationAssign'
        db.delete_table('mva_specialization_assign')

        # Deleting model 'Contact'
        db.delete_table('mva_contact')

        # Deleting model 'Badge'
        db.delete_table('mva_badge')

        # Deleting model 'BadgeAssign'
        db.delete_table('mva_badge_assign')

        # Deleting model 'Course'
        db.delete_table('mva_course')

        # Deleting model 'Section'
        db.delete_table('mva_section')

        # Deleting model 'SectionAssign'
        db.delete_table('mva_section_assign')

        # Deleting model 'Encouragement'
        db.delete_table('mva_encouragement')

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
            'difficulty': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.encouragement': {
            'Meta': {'object_name': 'Encouragement', 'db_table': "'mva_encouragement'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_from'", 'to': "orm['core.Profile']"}),
            'person_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_to'", 'to': "orm['core.Profile']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 3, 16, 55, 16, 14708)'})
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
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']", 'null': 'True', 'blank': 'True'}),
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
        'core.review': {
            'Meta': {'object_name': 'Review', 'db_table': "'mva_review'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'review_person_from'", 'to': "orm['core.Profile']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 3, 16, 55, 16, 15327)'})
        },
        'core.section': {
            'Meta': {'unique_together': "(('course', 'start_time', 'end_time'),)", 'object_name': 'Section', 'db_table': "'mva_section'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section_instructor'", 'to': "orm['core.Profile']"}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Profile']", 'through': "orm['core.SectionAssign']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
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

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'BadgeAssign', fields ['profile', 'badge']
        db.delete_unique('mva_badge_assign', ['profile_id', 'badge_id'])

        # Removing unique constraint on 'SkillAssign', fields ['profile', 'skill']
        db.delete_unique('mva_skill_assign', ['profile_id', 'skill_id'])

        # Removing unique constraint on 'SectionAssign', fields ['profile', 'section']
        db.delete_unique('mva_section_assign', ['profile_id', 'section_id'])

        # Removing unique constraint on 'SpecializationAssign', fields ['profile', 'specialization']
        db.delete_unique('mva_specialization_assign', ['profile_id', 'specialization_id'])

        # Deleting field 'SpecializationAssign.profile'
        db.delete_column('mva_specialization_assign', 'profile_id')

        # Adding field 'SpecializationAssign.user'
        db.add_column('mva_specialization_assign', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='specializationassign_user', to=orm['auth.User']), keep_default=False)

        # Adding unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.create_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Changing field 'Feedback.person_from'
        db.alter_column('mva_feedback', 'person_from_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Feedback.instructor'
        db.alter_column('mva_feedback', 'instructor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Encouragement.person_to'
        db.alter_column('mva_encouragement', 'person_to_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Encouragement.person_from'
        db.alter_column('mva_encouragement', 'person_from_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Deleting field 'SectionAssign.profile'
        db.delete_column('mva_section_assign', 'profile_id')

        # Adding field 'SectionAssign.user'
        db.add_column('mva_section_assign', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='sectionassign_user', to=orm['auth.User']), keep_default=False)

        # Adding unique constraint on 'SectionAssign', fields ['section', 'user']
        db.create_unique('mva_section_assign', ['section_id', 'user_id'])

        # Deleting field 'SkillAssign.profile'
        db.delete_column('mva_skill_assign', 'profile_id')

        # Adding field 'SkillAssign.user'
        db.add_column('mva_skill_assign', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='skillassign_user', to=orm['auth.User']), keep_default=False)

        # Adding unique constraint on 'SkillAssign', fields ['skill', 'user']
        db.create_unique('mva_skill_assign', ['skill_id', 'user_id'])

        # Changing field 'Review.person_from'
        db.alter_column('mva_review', 'person_from_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Report.reporter'
        db.alter_column('mva_report', 'reporter_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Deleting field 'BadgeAssign.profile'
        db.delete_column('mva_badge_assign', 'profile_id')

        # Adding field 'BadgeAssign.user'
        db.add_column('mva_badge_assign', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='badgeassign_user', to=orm['auth.User']), keep_default=False)

        # Adding unique constraint on 'BadgeAssign', fields ['badge', 'user']
        db.create_unique('mva_badge_assign', ['badge_id', 'user_id'])

        # Deleting field 'Contact.profile'
        db.delete_column('mva_contact', 'profile_id')

        # Adding field 'Contact.user'
        db.add_column('mva_contact', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']), keep_default=False)

        # Changing field 'Section.instructor'
        db.alter_column('mva_section', 'instructor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))


    def backwards(self, orm):
        
        # Removing unique constraint on 'BadgeAssign', fields ['badge', 'user']
        db.delete_unique('mva_badge_assign', ['badge_id', 'user_id'])

        # Removing unique constraint on 'SkillAssign', fields ['skill', 'user']
        db.delete_unique('mva_skill_assign', ['skill_id', 'user_id'])

        # Removing unique constraint on 'SectionAssign', fields ['section', 'user']
        db.delete_unique('mva_section_assign', ['section_id', 'user_id'])

        # Removing unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.delete_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Adding field 'SpecializationAssign.profile'
        db.add_column('mva_specialization_assign', 'profile', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='specializationassign_profile', to=orm['core.Profile']), keep_default=False)

        # Deleting field 'SpecializationAssign.user'
        db.delete_column('mva_specialization_assign', 'user_id')

        # Adding unique constraint on 'SpecializationAssign', fields ['profile', 'specialization']
        db.create_unique('mva_specialization_assign', ['profile_id', 'specialization_id'])

        # Changing field 'Feedback.person_from'
        db.alter_column('mva_feedback', 'person_from_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile']))

        # Changing field 'Feedback.instructor'
        db.alter_column('mva_feedback', 'instructor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile']))

        # Changing field 'Encouragement.person_to'
        db.alter_column('mva_encouragement', 'person_to_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile']))

        # Changing field 'Encouragement.person_from'
        db.alter_column('mva_encouragement', 'person_from_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile']))

        # Adding field 'SectionAssign.profile'
        db.add_column('mva_section_assign', 'profile', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='sectionassign_profile', to=orm['core.Profile']), keep_default=False)

        # Deleting field 'SectionAssign.user'
        db.delete_column('mva_section_assign', 'user_id')

        # Adding unique constraint on 'SectionAssign', fields ['profile', 'section']
        db.create_unique('mva_section_assign', ['profile_id', 'section_id'])

        # Adding field 'SkillAssign.profile'
        db.add_column('mva_skill_assign', 'profile', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='skillassign_profile', to=orm['core.Profile']), keep_default=False)

        # Deleting field 'SkillAssign.user'
        db.delete_column('mva_skill_assign', 'user_id')

        # Adding unique constraint on 'SkillAssign', fields ['profile', 'skill']
        db.create_unique('mva_skill_assign', ['profile_id', 'skill_id'])

        # Changing field 'Review.person_from'
        db.alter_column('mva_review', 'person_from_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile']))

        # Changing field 'Report.reporter'
        db.alter_column('mva_report', 'reporter_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Profile']))

        # Adding field 'BadgeAssign.profile'
        db.add_column('mva_badge_assign', 'profile', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='badgeassign_profile', to=orm['core.Profile']), keep_default=False)

        # Deleting field 'BadgeAssign.user'
        db.delete_column('mva_badge_assign', 'user_id')

        # Adding unique constraint on 'BadgeAssign', fields ['profile', 'badge']
        db.create_unique('mva_badge_assign', ['profile_id', 'badge_id'])

        # Adding field 'Contact.profile'
        db.add_column('mva_contact', 'profile', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Profile']), keep_default=False)

        # Deleting field 'Contact.user'
        db.delete_column('mva_contact', 'user_id')

        # Changing field 'Section.instructor'
        db.alter_column('mva_section', 'instructor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Profile']))


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
            'next_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'next_lvl': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'badge_next_lvl'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Badge']"}),
            'prev_lvl': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'badge_prev_lvl'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Badge']"}),
            'req_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['core.BadgeAssign']", 'symmetrical': 'False'})
        },
        'core.badgeassign': {
            'Meta': {'unique_together': "(('user', 'badge'),)", 'object_name': 'BadgeAssign', 'db_table': "'mva_badge_assign'"},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badgeassign_badge'", 'to': "orm['core.Badge']"}),
            'exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obtained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badgeassign_user'", 'to': "orm['auth.User']"})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "'mva_contact'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'province_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProvinceState']"}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'mva_country'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.course': {
            'Meta': {'unique_together': "(('title', 'abbrev', 'institute'),)", 'object_name': 'Course', 'db_table': "'mva_course'"},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 331987)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.encouragement': {
            'Meta': {'object_name': 'Encouragement', 'db_table': "'mva_encouragement'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_from'", 'to': "orm['auth.User']"}),
            'person_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_to'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 333484)'})
        },
        'core.feedback': {
            'Meta': {'object_name': 'Feedback', 'db_table': "'mva_feedback'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedback_person_from'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 334440)'})
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
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
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
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.report': {
            'Meta': {'object_name': 'Report', 'db_table': "'mva_report'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'report_reporter'", 'null': 'True', 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 334922)'})
        },
        'core.review': {
            'Meta': {'object_name': 'Review', 'db_table': "'mva_review'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'review_person_from'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 333959)'})
        },
        'core.section': {
            'Meta': {'unique_together': "(('course', 'first_day', 'last_day', 'instructor'),)", 'object_name': 'Section', 'db_table': "'mva_section'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'first_day': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section_instructor'", 'to': "orm['auth.User']"}),
            'last_day': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['core.SectionAssign']", 'symmetrical': 'False'})
        },
        'core.sectionassign': {
            'Meta': {'unique_together': "(('user', 'section'),)", 'object_name': 'SectionAssign', 'db_table': "'mva_section_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectionassign_section'", 'to': "orm['core.Section']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectionassign_user'", 'to': "orm['auth.User']"})
        },
        'core.skill': {
            'Meta': {'object_name': 'Skill', 'db_table': "'mva_skill'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 329350)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['core.SkillAssign']", 'symmetrical': 'False'})
        },
        'core.skillassign': {
            'Meta': {'unique_together': "(('user', 'skill'),)", 'object_name': 'SkillAssign', 'db_table': "'mva_skill_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skillassign_skill'", 'to': "orm['core.Skill']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skillassign_user'", 'to': "orm['auth.User']"})
        },
        'core.specialization': {
            'Meta': {'object_name': 'Specialization', 'db_table': "'mva_specialization'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 28, 1, 31, 7, 328488)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['core.SpecializationAssign']", 'symmetrical': 'False'})
        },
        'core.specializationassign': {
            'Meta': {'unique_together': "(('user', 'specialization'),)", 'object_name': 'SpecializationAssign', 'db_table': "'mva_specialization_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specializationassign_specialization'", 'to': "orm['core.Specialization']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specializationassign_user'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['core']

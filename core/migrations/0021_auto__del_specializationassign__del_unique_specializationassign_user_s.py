# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'BadgeAssign', fields ['user', 'badge']
        db.delete_unique('mva_badge_assign', ['user_id', 'badge_id'])

        # Removing unique constraint on 'SkillAssign', fields ['user', 'skill']
        db.delete_unique('mva_skill_assign', ['user_id', 'skill_id'])

        # Removing unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.delete_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Deleting model 'SpecializationAssign'
        db.delete_table('mva_specialization_assign')

        # Deleting model 'Feedback'
        db.delete_table('mva_feedback')

        # Deleting model 'Encouragement'
        db.delete_table('mva_encouragement')

        # Deleting model 'Profile'
        db.delete_table('mva_profile')

        # Deleting model 'Skill'
        db.delete_table('mva_skill')

        # Deleting model 'SkillAssign'
        db.delete_table('mva_skill_assign')

        # Deleting model 'Badge'
        db.delete_table('mva_badge')

        # Deleting model 'BadgeAssign'
        db.delete_table('mva_badge_assign')

        # Deleting model 'Contact'
        db.delete_table('mva_contact')

        # Deleting model 'Specialization'
        db.delete_table('mva_specialization')


    def backwards(self, orm):
        
        # Adding model 'SpecializationAssign'
        db.create_table('mva_specialization_assign', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_user', to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_specialization', to=orm['core.Specialization'])),
        ))
        db.send_create_signal('core', ['SpecializationAssign'])

        # Adding unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.create_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Adding model 'Feedback'
        db.create_table('mva_feedback', (
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 29, 22, 30, 41, 663846))),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedback_person_from', to=orm['auth.User'])),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Feedback'])

        # Adding model 'Encouragement'
        db.create_table('mva_encouragement', (
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 29, 22, 30, 41, 662871))),
            ('person_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_to', to=orm['auth.User'])),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_from', to=orm['auth.User'])),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Encouragement'])

        # Adding model 'Profile'
        db.create_table('mva_profile', (
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('tagline', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'], null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('influence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Profile'])

        # Adding model 'Skill'
        db.create_table('mva_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Skill'])

        # Adding model 'SkillAssign'
        db.create_table('mva_skill_assign', (
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skillassign_skill', to=orm['core.Skill'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skillassign_user', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['SkillAssign'])

        # Adding unique constraint on 'SkillAssign', fields ['user', 'skill']
        db.create_unique('mva_skill_assign', ['user_id', 'skill_id'])

        # Adding model 'Badge'
        db.create_table('mva_badge', (
            ('next_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('next_lvl', self.gf('django.db.models.fields.related.OneToOneField')(related_name='badge_next_lvl', unique=True, null=True, to=orm['core.Badge'], blank=True)),
            ('req_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('prev_lvl', self.gf('django.db.models.fields.related.OneToOneField')(related_name='badge_prev_lvl', unique=True, null=True, to=orm['core.Badge'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Badge'])

        # Adding model 'BadgeAssign'
        db.create_table('mva_badge_assign', (
            ('obtained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_user', to=orm['auth.User'])),
            ('exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_badge', to=orm['core.Badge'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['BadgeAssign'])

        # Adding unique constraint on 'BadgeAssign', fields ['user', 'badge']
        db.create_unique('mva_badge_assign', ['user_id', 'badge_id'])

        # Adding model 'Contact'
        db.create_table('mva_contact', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProvinceState'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Contact'])

        # Adding model 'Specialization'
        db.create_table('mva_specialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
        ))
        db.send_create_signal('core', ['Specialization'])


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
        'core.course': {
            'Meta': {'unique_together': "(('title', 'abbrev', 'institute'),)", 'object_name': 'Course', 'db_table': "'mva_course'"},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'core.review': {
            'Meta': {'object_name': 'Review', 'db_table': "'mva_review'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'review_person_from'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 29, 22, 56, 12, 957671)'})
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
        }
    }

    complete_apps = ['core']

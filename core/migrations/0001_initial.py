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
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
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

        # Adding model 'Specialization'
        db.create_table('mva_specialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Specialization'])

        # Adding model 'SpecializationAssign'
        db.create_table('mva_specialization_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_user', to=orm['auth.User'])),
            ('specialization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_specialization', to=orm['core.Specialization'])),
        ))
        db.send_create_signal('core', ['SpecializationAssign'])

        # Adding unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.create_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Adding model 'Skill'
        db.create_table('mva_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Skill'])

        # Adding model 'SkillAssign'
        db.create_table('mva_skill_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skillassign_user', to=orm['auth.User'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skillassign_skill', to=orm['core.Skill'])),
        ))
        db.send_create_signal('core', ['SkillAssign'])

        # Adding unique constraint on 'SkillAssign', fields ['user', 'skill']
        db.create_unique('mva_skill_assign', ['user_id', 'skill_id'])

        # Adding model 'Badge'
        db.create_table('mva_badge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('prev_lvl', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='badge_prev_lvl', unique=True, null=True, to=orm['core.Badge'])),
            ('req_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('next_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('next_lvl', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='badge_next_lvl', unique=True, null=True, to=orm['core.Badge'])),
        ))
        db.send_create_signal('core', ['Badge'])

        # Adding model 'BadgeAssign'
        db.create_table('mva_badge_assign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_user', to=orm['auth.User'])),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_badge', to=orm['core.Badge'])),
            ('obtained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['BadgeAssign'])

        # Adding unique constraint on 'BadgeAssign', fields ['user', 'badge']
        db.create_unique('mva_badge_assign', ['user_id', 'badge_id'])

        # Adding model 'Encouragement'
        db.create_table('mva_encouragement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_to', to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_from', to=orm['auth.User'])),
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Encouragement'])

        # Adding model 'Feedback'
        db.create_table('mva_feedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedback_person_from', to=orm['auth.User'])),
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('core', ['Feedback'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'BadgeAssign', fields ['user', 'badge']
        db.delete_unique('mva_badge_assign', ['user_id', 'badge_id'])

        # Removing unique constraint on 'SkillAssign', fields ['user', 'skill']
        db.delete_unique('mva_skill_assign', ['user_id', 'skill_id'])

        # Removing unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.delete_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Deleting model 'Country'
        db.delete_table('mva_country')

        # Deleting model 'ProvinceState'
        db.delete_table('mva_province_state')

        # Deleting model 'Institute'
        db.delete_table('mva_institute')

        # Deleting model 'Specialization'
        db.delete_table('mva_specialization')

        # Deleting model 'SpecializationAssign'
        db.delete_table('mva_specialization_assign')

        # Deleting model 'Skill'
        db.delete_table('mva_skill')

        # Deleting model 'SkillAssign'
        db.delete_table('mva_skill_assign')

        # Deleting model 'Badge'
        db.delete_table('mva_badge')

        # Deleting model 'BadgeAssign'
        db.delete_table('mva_badge_assign')

        # Deleting model 'Encouragement'
        db.delete_table('mva_encouragement')

        # Deleting model 'Feedback'
        db.delete_table('mva_feedback')


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
        'core.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'mva_country'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.encouragement': {
            'Meta': {'object_name': 'Encouragement', 'db_table': "'mva_encouragement'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_from'", 'to': "orm['auth.User']"}),
            'person_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_to'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'core.feedback': {
            'Meta': {'object_name': 'Feedback', 'db_table': "'mva_feedback'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedback_person_from'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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
        'core.skill': {
            'Meta': {'object_name': 'Skill', 'db_table': "'mva_skill'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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

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

        # Deleting model 'Specialization'
        db.delete_table('mva_specialization')

        # Deleting model 'Encouragement'
        db.delete_table('mva_encouragement')

        # Deleting model 'Badge'
        db.delete_table('mva_badge')

        # Deleting model 'SpecializationAssign'
        db.delete_table('mva_specialization_assign')

        # Deleting model 'SkillAssign'
        db.delete_table('mva_skill_assign')

        # Deleting model 'Skill'
        db.delete_table('mva_skill')

        # Deleting model 'Feedback'
        db.delete_table('mva_feedback')

        # Deleting model 'BadgeAssign'
        db.delete_table('mva_badge_assign')


    def backwards(self, orm):
        
        # Adding model 'Specialization'
        db.create_table('mva_specialization', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['Specialization'])

        # Adding model 'Encouragement'
        db.create_table('mva_encouragement', (
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('person_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_to', to=orm['auth.User'])),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encouragement_person_from', to=orm['auth.User'])),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['Encouragement'])

        # Adding model 'Badge'
        db.create_table('mva_badge', (
            ('next_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('next_lvl', self.gf('django.db.models.fields.related.OneToOneField')(related_name='badge_next_lvl', unique=True, null=True, to=orm['account.Badge'], blank=True)),
            ('req_exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('prev_lvl', self.gf('django.db.models.fields.related.OneToOneField')(related_name='badge_prev_lvl', unique=True, null=True, to=orm['account.Badge'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['Badge'])

        # Adding model 'SpecializationAssign'
        db.create_table('mva_specialization_assign', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_user', to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specializationassign_specialization', to=orm['account.Specialization'])),
        ))
        db.send_create_signal('account', ['SpecializationAssign'])

        # Adding unique constraint on 'SpecializationAssign', fields ['user', 'specialization']
        db.create_unique('mva_specialization_assign', ['user_id', 'specialization_id'])

        # Adding model 'SkillAssign'
        db.create_table('mva_skill_assign', (
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skillassign_skill', to=orm['account.Skill'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skillassign_user', to=orm['auth.User'])),
        ))
        db.send_create_signal('account', ['SkillAssign'])

        # Adding unique constraint on 'SkillAssign', fields ['user', 'skill']
        db.create_unique('mva_skill_assign', ['user_id', 'skill_id'])

        # Adding model 'Skill'
        db.create_table('mva_skill', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['Skill'])

        # Adding model 'Feedback'
        db.create_table('mva_feedback', (
            ('sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('person_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedback_person_from', to=orm['auth.User'])),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['Feedback'])

        # Adding model 'BadgeAssign'
        db.create_table('mva_badge_assign', (
            ('obtained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_user', to=orm['auth.User'])),
            ('exp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badgeassign_badge', to=orm['account.Badge'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['BadgeAssign'])

        # Adding unique constraint on 'BadgeAssign', fields ['user', 'badge']
        db.create_unique('mva_badge_assign', ['user_id', 'badge_id'])


    models = {
        'account.contact': {
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
        'account.profile': {
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
        }
    }

    complete_apps = ['account']

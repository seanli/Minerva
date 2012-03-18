# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Specialization.created_time'
        db.add_column('mva_specialization', 'created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2012, 3, 18), blank=True), keep_default=False)

        # Changing field 'Encouragement.sent_time'
        db.alter_column('mva_encouragement', 'sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Adding field 'Skill.created_time'
        db.add_column('mva_skill', 'created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2012, 3, 18), blank=True), keep_default=False)

        # Changing field 'Feedback.sent_time'
        db.alter_column('mva_feedback', 'sent_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Deleting field 'Specialization.created_time'
        db.delete_column('mva_specialization', 'created_time')

        # Changing field 'Encouragement.sent_time'
        db.alter_column('mva_encouragement', 'sent_time', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'Skill.created_time'
        db.delete_column('mva_skill', 'created_time')

        # Changing field 'Feedback.sent_time'
        db.alter_column('mva_feedback', 'sent_time', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'account.badge': {
            'Meta': {'object_name': 'Badge', 'db_table': "'mva_badge'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'next_lvl': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'badge_next_lvl'", 'unique': 'True', 'null': 'True', 'to': "orm['account.Badge']"}),
            'prev_lvl': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'badge_prev_lvl'", 'unique': 'True', 'null': 'True', 'to': "orm['account.Badge']"}),
            'req_exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['account.BadgeAssign']", 'symmetrical': 'False'})
        },
        'account.badgeassign': {
            'Meta': {'unique_together': "(('user', 'badge'),)", 'object_name': 'BadgeAssign', 'db_table': "'mva_badge_assign'"},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badgeassign_badge'", 'to': "orm['account.Badge']"}),
            'exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obtained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badgeassign_user'", 'to': "orm['auth.User']"})
        },
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
        'account.encouragement': {
            'Meta': {'object_name': 'Encouragement', 'db_table': "'mva_encouragement'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_from'", 'to': "orm['auth.User']"}),
            'person_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encouragement_person_to'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'account.feedback': {
            'Meta': {'object_name': 'Feedback', 'db_table': "'mva_feedback'"},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'person_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedback_person_from'", 'to': "orm['auth.User']"}),
            'sent_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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
        'account.skill': {
            'Meta': {'object_name': 'Skill', 'db_table': "'mva_skill'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['account.SkillAssign']", 'symmetrical': 'False'})
        },
        'account.skillassign': {
            'Meta': {'unique_together': "(('user', 'skill'),)", 'object_name': 'SkillAssign', 'db_table': "'mva_skill_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skillassign_skill'", 'to': "orm['account.Skill']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skillassign_user'", 'to': "orm['auth.User']"})
        },
        'account.specialization': {
            'Meta': {'object_name': 'Specialization', 'db_table': "'mva_specialization'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['account.SpecializationAssign']", 'symmetrical': 'False'})
        },
        'account.specializationassign': {
            'Meta': {'unique_together': "(('user', 'specialization'),)", 'object_name': 'SpecializationAssign', 'db_table': "'mva_specialization_assign'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specializationassign_specialization'", 'to': "orm['account.Specialization']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specializationassign_user'", 'to': "orm['auth.User']"})
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

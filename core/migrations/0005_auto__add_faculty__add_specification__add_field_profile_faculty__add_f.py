# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Faculty'
        db.create_table('mva_faculty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Institute'])),
        ))
        db.send_create_signal('core', ['Faculty'])

        # Adding model 'Specification'
        db.create_table('mva_specification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Specification'])

        # Adding field 'Profile.faculty'
        db.add_column('mva_profile', 'faculty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Faculty'], null=True, blank=True), keep_default=False)

        # Adding field 'Profile.specification'
        db.add_column('mva_profile', 'specification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Specification'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Faculty'
        db.delete_table('mva_faculty')

        # Deleting model 'Specification'
        db.delete_table('mva_specification')

        # Deleting field 'Profile.faculty'
        db.delete_column('mva_profile', 'faculty_id')

        # Deleting field 'Profile.specification'
        db.delete_column('mva_profile', 'specification_id')


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
        'core.faculty': {
            'Meta': {'object_name': 'Faculty', 'db_table': "'mva_faculty'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
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
        'core.profile': {
            'Meta': {'object_name': 'Profile', 'db_table': "'mva_profile'"},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Faculty']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instutute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Institute']"}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'specification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Specification']", 'null': 'True', 'blank': 'True'}),
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
        'core.specification': {
            'Meta': {'object_name': 'Specification', 'db_table': "'mva_specification'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']

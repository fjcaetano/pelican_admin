# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Settings'
        db.create_table('pelican_admin_settings', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32, primary_key=True)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pelican_admin', ['Settings'])

        # Adding model 'BlogPost'
        db.create_table('pelican_admin_blogpost', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('markup', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('file_path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, primary_key=True)),
        ))
        db.send_create_signal('pelican_admin', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table('pelican_admin_settings')

        # Deleting model 'BlogPost'
        db.delete_table('pelican_admin_blogpost')


    models = {
        'pelican_admin.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'markup': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pelican_admin.settings': {
            'Meta': {'ordering': "['name']", 'object_name': 'Settings'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['pelican_admin']
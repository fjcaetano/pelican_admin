# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.status'
        db.add_column('pelican_admin_blogpost', 'status',
                      self.gf('django.db.models.fields.CharField')(default='published', max_length=127),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.status'
        db.delete_column('pelican_admin_blogpost', 'status')


    models = {
        'pelican_admin.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author': ('django.db.models.fields.CharField', [], {'default': 'u"u\'Fl\\\\xe1vio Caetano\'"', 'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pelican_admin.Category']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': 'u"u\'br\'"', 'max_length': '5', 'blank': 'True'}),
            'markup': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'published'", 'max_length': '127'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '511', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pelican_admin.category': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pelican_admin.settings': {
            'Meta': {'ordering': "['name']", 'object_name': 'Settings'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['pelican_admin']
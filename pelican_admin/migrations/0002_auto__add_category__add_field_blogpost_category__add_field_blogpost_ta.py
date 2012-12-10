# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('pelican_admin_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('pelican_admin', ['Category'])

        # Adding field 'BlogPost.category'
        db.add_column('pelican_admin_blogpost', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pelican_admin.Category'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.tags'
        db.add_column('pelican_admin_blogpost', 'tags',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.slug'
        db.add_column('pelican_admin_blogpost', 'slug',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.author'
        db.add_column('pelican_admin_blogpost', 'author',
                      self.gf('django.db.models.fields.CharField')(default=u'Fl\xe1vio Caetano', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.summary'
        db.add_column('pelican_admin_blogpost', 'summary',
                      self.gf('django.db.models.fields.CharField')(max_length=511, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.lang'
        db.add_column('pelican_admin_blogpost', 'lang',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=5, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('pelican_admin_category')

        # Deleting field 'BlogPost.category'
        db.delete_column('pelican_admin_blogpost', 'category_id')

        # Deleting field 'BlogPost.tags'
        db.delete_column('pelican_admin_blogpost', 'tags')

        # Deleting field 'BlogPost.slug'
        db.delete_column('pelican_admin_blogpost', 'slug')

        # Deleting field 'BlogPost.author'
        db.delete_column('pelican_admin_blogpost', 'author')

        # Deleting field 'BlogPost.summary'
        db.delete_column('pelican_admin_blogpost', 'summary')

        # Deleting field 'BlogPost.lang'
        db.delete_column('pelican_admin_blogpost', 'lang')


    models = {
        'pelican_admin.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author': ('django.db.models.fields.CharField', [], {'default': "u'Fl\\xe1vio Caetano'", 'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pelican_admin.Category']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '5', 'blank': 'True'}),
            'markup': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
__author__ = 'Flavio'

from django.db import models
from django.conf import settings

import os, sys, pprint

from pelican_admin import get_pelican_settings

class Settings(models.Model):

    name = models.CharField(max_length=32, unique=True, primary_key=True)

    value = models.TextField()

    def save(self, **kwargs):
        super(Settings, self).save(**kwargs)

        pelican_settings_name = get_pelican_settings()
        f = open(os.path.join(settings.PELICAN_PATH, pelican_settings_name+'.py'), 'w')

        f.write('#coding: utf-8\n\n')

        all_objs = Settings.objects.all()

        for set in all_objs:
            f.write('%s = %s\n' % (set.name, set.value))

        f.close()

    @classmethod
    def load_from_path(cls):
        pelican_settings_name = get_pelican_settings()

        sys.path.append(settings.PELICAN_PATH)
        pelican_settings = None

        exec 'import %s; pelican_settings = %s' % (pelican_settings_name, pelican_settings_name) in None

        attr_list = dir(pelican_settings)
        user_settings = dict((attr, getattr(pelican_settings, attr)) for attr in attr_list if not attr.startswith('__'))

        default = {
            'AUTHOR': None,
            'TIMEZONE': None,
            'DATE_FORMAT': {},
            'USE_FOLDER_AS_CATEGORY': True,
            'DEFAULT_CATEGORY': 'misc',
            'DAFAULT_DATE_FORMAT': '%a %d %B %Y',
            'DISPLAY_PAGES_ON_MENU': True,
            'DEFAULT_DATE': 'fs',
            'DELETE_OUTPUT_COPY': False,
            'FILES_TO_COPY': tuple(),
            'JINJA_EXTENSIONS': [],
            'LOCALE': '',
            'MARKUP': ('rst', 'md'),
            'MD_EXTENSIONS': ['codehilite', 'extra'],
            'OUTPUT_PATH': 'output/',
            'PATH': settings.PELICAN_PATH,
            'PAGE_DIR': 'pages',
            'PAGE_EXCLUDES': tuple(),
            'ARTICLE_DIR': '',
            'ARTICLE_EXCLUDES': ('pages',),
            'PDF_GENERATOR': False,
            'OUTPUT_SOURCES': True,
            'OUTPUT_SOURCES_EXTENSION': '.text',
            'RELATIVE_URLS': True,
            'PLUGINS': [],
            'SITENAME': 'A Pelican Blog',
            'TEMPLATE_PAGES': None,
            'STATIC_PATHS': ['images'],
            'TYPOGRAFY': False,
            'DIRECT_TEMPLATES': ('index', 'tags', 'categories', 'archives'),
            'PAGINATED_DIRECT_TEMPLATES': ('index',),
            'SUMMARY_MAX_LENGTH': 50,
            'EXTRA_TEMPLATES_PATHS': [],
            'MARKDOWN_EXTENSIONS': ['toc'],
            'ARTICLE_URL': '{slug}.html',
            'ARTICLE_SAVE_AS': '{slug}.html',
            'ARTICLE_LANG_URL': '{slug}-{lang}.html',
            'ARTICLE_LANG_SAVE_AS': '{slug}-{lang}.html',
            'PAGE_URL': 'pages/{slug}.html',
            'PAGE_SAVE_AS': 'pages/{slug}.html',
            'PAGE_LANG_URL': 'pages/{slug}-{lang}.html',
            'PAGE_LANG_SAVE_AS': 'pages/{slug}-{lang}.html',
            'AUTHOR_URL': 'author/{slug}.html',
            'AUTHOR_SAVE_AS': 'author/{slug}.html',
            'CATEGORY_URL': 'category/{slug}.html',
            'CATEGORY_SAVE_AS': 'category/{slug}.html',
            'TAG_URL': 'tag/{slug}.html',
            'TAG_SAVE_AS': 'tag/{slug}.html',
            'FEED_DOMAIN': None,
            'FEED_ATOM': None,
            'FEED_RSS': None,
            'FEED_ALL_ATOM': 'feeds/all.atom.xml',
            'FEED_ALL_RSS': None,
            'CATEGORY_FEED_ATOM': 'feeds/%s.atom.xml',
            'CATEGORY_FEED_RSS': None,
            'TAG_FEED_ATOM': None,
            'TAG_FEED_RSS': None,
            'FEED_MAX_ITEMS': None,
            'DEFAULT_ORPHANS': 0,
            'DEFAULT_PAGINATION': False,
            'TAG_CLOUD_STEPS': 4,
            'TAG_CLOUD_MAX_ITEMS': 100,
            'DEFAULT_LANG': 'en',
            'TRANSLATION_FEED_ATOM': 'feeds/all-%s.atom.xml',
            'TRANSLATION_FEED_RSS': None,
            'NEWEST_FIRST_ARCHIVES': True,
            'REVERSE_CATEGORY_ORDER': False,
            'THEME': 'notmyidea',
            'THEME_STATIC_PATHS': ['static'],
            'CSS_FILE': 'main.css',
            'DISQUS_SITENAME': None,
            'GITHUB_URL': None,
            'GOOGLE_ANALYTICS': None,
            'GOSQUARED_SITENAME': None,
            'MENUITEMS': tuple(),
            'PIWIKI_URL': None,
            'PIWIKI_SSL_URL': None,
            'PIWIKI_SITE_ID': None,
            'LINKS': None,
            'SOCIAL': None,
            'TWITTER_USERNAME': None,
            'DEFAULT_METADATA': tuple()
        }

        default = dict(default.items() + user_settings.items())

        for attr, def_value in default.items():
            attr_value = pprint.pformat(def_value)

            set = Settings(name=attr, value=attr_value)
            set.save()

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Settings'
        ordering = ['name']
        app_label = 'pelican_admin'
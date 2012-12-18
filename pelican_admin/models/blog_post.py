__author__ = 'Flavio'

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from pelican.utils import slugify

from pelican_admin.models import Settings, Category

import os, datetime, codecs

MARKUPS = (
    (0, 'rst'),
    (1, 'md'),
)

STATUS = (
    ('published', _('Published')),
    ('draft', _('Draft')),
    ('hidden', _('Hidden')),
)

def _pelican_setting(name):
    try:
        return Settings.objects.get(name=name).value
    except Settings.DoesNotExist:
        return ''

class BlogPost(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    markup = models.SmallIntegerField(_('Markup'), choices=MARKUPS, default=0)

    category = models.ForeignKey('Category', null=True, blank=True)

    # Metadatas
    text = models.TextField(_('Text'))
    date = models.DateTimeField(_('Date'), default=datetime.datetime.now)
    tags = models.CharField(_('Tags'), max_length=255, null=True, blank=True)
    slug = models.CharField(_('Slug'), max_length=255, null=True, blank=True)
    author = models.CharField(_('Author'), max_length=255, default=_pelican_setting('AUTHOR'))
    summary = models.CharField(_('Summary'), max_length=511, null=True, blank=True)
    lang = models.CharField(_('Language'), max_length=5, default=_pelican_setting('DEFAULT_LANG'))
    status = models.CharField(_('Status'), choices=STATUS, default='published', max_length=127)

    file_path = models.CharField(_('File Path'), max_length=255, unique=True, primary_key=True)

    def save(self, **kwargs):
        self.write()

        super(BlogPost, self).save(**kwargs)

    def write(self):
        if not self.file_path:
            filename ='%s.%s' % (self.get_slug(), MARKUPS[self.markup][1])
            self.file_path = os.path.join(settings.PELICAN_PATH, 'content', filename)

        f = codecs.open(self.file_path, 'w', encoding="utf-8")

        meta_format = '%s: %s\n'

        title_meta = meta_format % (self.metafy('title'), self.title)
        f.write(title_meta)

        date_meta = meta_format % (self.metafy('date'), self.date.strftime('%Y-%m-%d %H:%M'))
        f.write(date_meta)

        author_meta = meta_format % (self.metafy('author'), self.author)
        f.write(author_meta)

        lang_meta = meta_format % (self.metafy('lang'), self.lang)
        f.write(lang_meta)

        status_meta = meta_format % (self.metafy('status'), self.status)
        f.write(status_meta)

        if self.tags:
            tags_meta = meta_format % (self.metafy('tags'), self.tags)
            f.write(tags_meta)

        if self.category:
            category_meta = meta_format % (self.metafy('category'), self.category)
            f.write(category_meta)

        if self.slug:
            slug_meta = meta_format % (self.metafy('slug'), self.slug)
            f.write(slug_meta)

        if self.summary:
            summary_meta = meta_format % (self.metafy('summary'), self.summary)
            f.write(summary_meta)

        f.write(self.text)
        f.close()

    def delete(self, using=None):
        os.remove(self.file_path)

        super(BlogPost, self).delete(using)

    def metafy(self, meta):
        return ':' + meta.lower() if self.markup == 0 else meta.title()

    def get_slug(self):
        if not self.slug:
            self.slug = slugify(self.title)

        return self.slug

    @classmethod
    def get_from_meta(cls, markup, title=None, slug=None):
        content_path = os.path.join(settings.PELICAN_PATH, 'content')

        if isinstance(markup, int):
            markup = MARKUPS[markup][1]

        if slug:
            file_path = os.path.join(content_path, slug+'.'+markup)
            try:
                result = BlogPost.objects.get(file_path=file_path)
                return result
            except BlogPost.DoesNotExist:
                pass

        if title:
            file_path = os.path.join(content_path, slugify(title)+'.'+markup)
            try:
                result = BlogPost.objects.get(file_path=file_path)
                return result
            except BlogPost.DoesNotExist:
                pass

        raise BlogPost.DoesNotExist()

    @classmethod
    def load_posts(cls):
        BlogPost.objects.all().delete()

        post_model_list = []

        content_path = os.path.join(settings.PELICAN_PATH, 'content')
        for file in os.listdir(content_path):
            post = BlogPost()
            post.file_path = os.path.join(content_path, file)

            if file.endswith('.rst'):
                post.markup = 0

            elif file.endswith('.md'):
                post.markup = 1

            f = open(post.file_path, 'r+')

            for line in f.readlines():
                parse = lambda meta: line.split(post.metafy(meta)+':')[1].strip()

                if line.startswith(post.metafy('title')):
                    post.title = parse('title')

                elif line.startswith(post.metafy('date')):
                    date_str = parse('date')
                    post.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')

                elif line.startswith(post.metafy('author')):
                    post.author = parse('author')

                elif line.startswith(post.metafy('lang')):
                    post.lang = parse('lang')

                elif line.startswith(post.metafy('status')):
                    post.status = parse('status')

                elif line.startswith(post.metafy('tags')):
                    post.tags = parse('tags')

                elif line.startswith(post.metafy('category')):
                    category_str = parse('category')
                    post.category = Category.objects.get_or_create(name=category_str)

                elif line.startswith(post.metafy('slug')):
                    post.slug = parse('slug')

                elif line.startswith(post.metafy('summary')):
                    post.summary = parse('summary')

                else:
                    post.text += line

            post_model_list.append(post)

        BlogPost.objects.bulk_create(post_model_list)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        app_label = 'pelican_admin'

        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')
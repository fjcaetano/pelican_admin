__author__ = 'Flavio'

from django.db import models
from django.conf import settings

import os, datetime

MARKUPS = (
    (0, 'rst'),
    (1, 'md'),
)

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    markup = models.SmallIntegerField(choices=MARKUPS, default=0)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)

    file_path = models.CharField(max_length=255, unique=True, primary_key=True)

    def save(self, **kwargs):
        super(BlogPost, self).save(**kwargs)

        f = open(self.file_path, 'w')

        f.write('%s: %s\n' % (self.metafy('title'), self.title))
        f.write('%s: %s\n' % (self.metafy('date'), self.date.strftime('%Y-%m-%d %H:%M')))
        f.write(self.text)

        f.close()

    def delete(self, using=None):
        os.remove(self.file_path)

        super(BlogPost, self).delete(using)

    def metafy(self, meta):
        return ':' + meta.lower() if self.markup == 0 else meta.title()

    @classmethod
    def load_posts(cls):
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
                if line.startswith('Title:') or line.startswith(':title:'):
                    post.title = line.split(post.metafy('title')+':')[1].strip()

                elif line.startswith('Date:') or line.startswith(':date:'):
                    date_str = line.split(post.metafy('date')+':')[1].strip()
                    post.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')

                else:
                    post.text += line

            post_model_list.append(post)

        for post in post_model_list:
            post.save()

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        app_label = 'pelican_admin'
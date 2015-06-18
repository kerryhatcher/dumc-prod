__author__ = 'kwhatcher'

from flask import url_for
from churchrunner import db

class Role(db.Document):
    name = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name


    meta = {
        'allow_inheritance': True,
        'indexes': ['-name', 'slug'],
        'ordering': ['-name']
    }



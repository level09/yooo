from extensions import db
import datetime
import json

class Link(db.Document):
    lid = db.SequenceField(unique=True)
    longUrl = db.StringField()
    shortUrl = db.StringField()
    date_submitted = db.DateTimeField(default=datetime.datetime.now)
    usage = db.IntField(default=0)

    def __unicode__(self):
        return '%s' % self.longUrl
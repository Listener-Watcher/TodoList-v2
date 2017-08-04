from django.db import models
# from __future__ import unicode_literals
from datetime import datetime
# Create your models here.
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    deadline = models.DateTimeField(default=datetime.now)
    priority = models.IntegerField(default=0)
    text = models.TextField()
    done = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title

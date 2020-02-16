from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    visible = models.BooleanField(default=True, null=False, blank=False)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    content = models.TextField()
    created_time = models.DateTimeField()
    visible = models.BooleanField(default=True, null=False, blank=False)
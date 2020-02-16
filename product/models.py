from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    visible = models.BooleanField(default=True, null=False, blank=False)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    image = models.ImageField(upload_to='product')
    visible = models.BooleanField(default=True, null=False, blank=False)
    created_time = models.DateTimeField(null=False, default=datetime.now())
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title
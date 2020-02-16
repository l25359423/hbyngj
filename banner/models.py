from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='banner')
    visible = models.BooleanField(default=True, null=False, blank=False)
    weight = models.IntegerField(default=0)

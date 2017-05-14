# coding=utf-8
from __future__ import unicode_literals

import datetime
from django.db import models


# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    expire_date = models.DateField(default="")
    finished = models.BooleanField(default=False)
    PRIORITIES = (
        (0, 'VeryLow'),
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
        (4, 'Very High')
    )
    priority = models.IntegerField(default=0, choices=PRIORITIES)

    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

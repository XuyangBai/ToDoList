# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    expire_date = models.DateField(default='')
    owner = models.ForeignKey('auth.User',related_name='task',on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #
    #     super(task,self).save(*args, **kwargs)

    class Meta:
        ordering =('created',)
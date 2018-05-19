from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Book (models.Model):
    TYPE_BOOK_CHOICES = (
        ('one of novel', 'One of novel'),
        ('documentation', 'Documentation'),
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.DateField()
    number_of_pages = models.IntegerField(blank=True)
    type_of_book = models.CharField(max_length=200, choices=TYPE_BOOK_CHOICES)

    def __unicode__(self):
        return self.nama
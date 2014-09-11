# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=150)
    capital = models.ForeignKey(Capital)
    president = models.ForeignKey(Presidents)
    about_country = models.TextField()


class Presidents(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()
    photo = models.ImageField(verbose_name='Photo')

class Capital(models.Model):
    name = models.CharField(max_length=200)

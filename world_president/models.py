# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Capital(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Presidents(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()
    photo = models.ImageField(upload_to="photos")
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    birthday = models.DateField(null=True)
    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=150)
    capital = models.ForeignKey(Capital)
    president = models.ForeignKey(Presidents)
    about_country = models.TextField()
    flag = models.ImageField(upload_to='flags')

    def __unicode__(self):
        return self.name





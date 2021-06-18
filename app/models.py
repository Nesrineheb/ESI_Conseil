# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Logistique(models.Model):
    """
    La représentation d'un projet dans le système.
    Un projet est pris en charge par une équipe.
    """
    DateReunion= models.DateField
    SalleReunion= models.CharField(max_length=150)
    Transport= models.CharField(max_length=150)
    Nouriture= models.CharField(max_length=150)
    


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

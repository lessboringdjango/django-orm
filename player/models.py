from __future__ import unicode_literals

from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza)
    name = models.CharField(max_length=255)

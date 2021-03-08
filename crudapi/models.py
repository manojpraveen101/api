from django.db import models


class Employee(models.Model):
    firstname = models.CharField(max_length=70, blank=False, default='')
    lastname = models.CharField(max_length=200, blank=False, default='')




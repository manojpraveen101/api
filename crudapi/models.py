from django.db import models



class Employee(models.Model):
    firstname = models.CharField(max_length=70, blank=False, default='')
    lastname = models.CharField(max_length=200, blank=False, default='')
    #company = models.ForeignKey(Companyinfo, on_delete=models.CASCADE)

class Companyinfo(models.Model):
    companyname = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')




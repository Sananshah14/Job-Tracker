# jobs/models.py

from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    application_date = models.DateField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

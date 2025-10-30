from django.db import models

# Create your models here.
"""
Defines hospital departments ( Cardiology, Surgery)
Purpose : organize doctors into departments
Relationship: Used by doctors and nurses
"""
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

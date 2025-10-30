from django.db import models
from patient.models import Patient
from doctor.models import Doctor

# Create your models here.
"""
Keep log of multiple treatment overtime
"""

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    visit_date = models.DateField(auto_now_add=True)

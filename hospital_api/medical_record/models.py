from django.db import models
from patient.models import Patient
from doctor.models import Doctor, Nurse


# Create your models here.
"""
Keep log of multiple treatment overtime
"""

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    visit_date = models.DateField(auto_now_add=True)

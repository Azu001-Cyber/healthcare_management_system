from django.db import models
from appointment.models import Appointment
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.
"""
Records Medicines prescribed during appointment
Purpose: Link each prescription to a specific appointment.
Realtionship: appointment, doctor, and patient
"""
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    prescribed_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_datails = models.TextField( help_text='e.g Drug name, dosage, duration')
    created_at = models.DateTimeField(auto_now_add=True)
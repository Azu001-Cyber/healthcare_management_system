from django.db import models
from appointment.models import Appointment
from doctor.models import Doctor
from patient.models import Patient
from medical_record.models import MedicalRecord

# Create your models here.
"""
Records Medicines prescribed during appointment
Purpose: Link each prescription to a specific appointment.
Realtionship: appointment, doctor, and patient
"""
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT, related_name='prescriptions')
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.PROTECT, null=True, related_name='prescriptions')
    medication_datails = models.TextField( help_text='e.g Drug name, dosage, duration')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Prescription for {self.appointment.patient.first_name} by Dr.{self.appointment.doctor.first_name} on {self.created_at.date()}"
    

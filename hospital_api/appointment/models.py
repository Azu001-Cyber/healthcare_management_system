from django.db import models
from patient.models import Patient
from doctor.models import Doctor

# Create your models here.
"""
connects doctors and patient for specific consultations
Purpose: Schedule and track appointments.
Relationship: Doctor and Patient
"""

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='pending')
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

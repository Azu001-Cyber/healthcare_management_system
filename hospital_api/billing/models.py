from django.db import models
from patient.models import Patient
from appointment.models import Appointment 
# Create your models here.

"""
handels hospital billing for patients
Purpose: Track payments and total charges
Relationship: Connected to both appointment and patient
"""
PAYMENT_STATUS = [
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
]

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(choices=PAYMENT_STATUS, default='unpaid')
    issued_date = models.DateTimeField(auto_now_add=True)
from django.db import models
from user.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

"""
Stores patient specific data
Purpose: Contains patient details and medical history
Relationship: Linked to appointments, prescription, and billing.
"""

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth = models.DateField()
    location = models.TextField()
    blood_group = models.CharField(max_length=3, blank=True)
    medical_history = models.TextField(blank=True, null=True)
    emergency_contact = PhoneNumberField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'Patient {self.user.get_full_name} Profile'
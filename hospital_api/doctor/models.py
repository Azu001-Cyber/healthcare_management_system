from django.db import models
from user.models import CustomUser
from department.models import Department
"""
Holds data specific to doctors.
Purpose: Manage doctor information and assign them to departments
Relationship: Linked to Department
"""
# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization  = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"


class Nurse(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    years_of_experience = models.PositiveIntegerField(default=0)
    availability_status =  models.BooleanField(default=True)
    on_call = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return f"Nurse {self.user.get_full_name()}"

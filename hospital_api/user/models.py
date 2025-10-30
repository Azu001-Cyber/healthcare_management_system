from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

"""
Purpose: Centralized authentication for all users
Relationship: Each role (Doctor, Patient, Nurse) will have a one to one link to this base user
"""

    

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        #ensure email is provided
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        # create user object but not saved
        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password) #hash password
        user.save()
        return user
    
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        # 1️⃣ Add default admin privileges
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        # 2️⃣ Call create_user() to reuse logic
        return self.create_user(username, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('nurse', 'Nurse'),
    ]
    objects = CustomUserManager()
    image = models.ImageField(upload_to='pfp/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField(max_length=15, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.is_admin = self.role == 'admin'
        self.is_doctor = self.role == 'doctor'
        self.is_nurse = self.role == 'nurse'
        self.is_patient = self.role == 'patient'
        super().save(*args, **kwargs)
    
    def user_handel(self):
        return f'@{self.username}'
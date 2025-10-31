from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
# Create your models here.

"""
Purpose: Centralized authentication for all users
Relationship: Each role (Doctor, Patient, Nurse) will have a one to one link to this base user
"""

def upload_to(instance, filename):
    slug_name = slugify(instance.name)
    return f'pfp/{slug_name}/{filename}'

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
        # Add default admin privileges
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        # Call create_user() to reuse logic
        return self.create_user(username, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('nurse', 'Nurse'),
    ]
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField(max_length=15, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.is_admin = self.role == 'admin'
        self.is_doctor = self.role == 'doctor'
        self.is_nurse = self.role == 'nurse'
        self.is_patient = self.role == 'patient'
        super().save(*args, **kwargs)
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
        
    role = instance.role

    if role == 'patient':
        from patient.models import Patient
        Patient.objects.create(user=instance)

    elif role == 'doctor':
        from doctor.models import Doctor
        Doctor.objects.create(user=instance)

    elif role == 'nurse':
        from  doctor.models import Nurse
        Nurse.objects.create(user=instance)


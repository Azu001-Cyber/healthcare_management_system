
from rest_framework import serializers
from .models import Doctor, Nurse

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"
    

class NurseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nurse
        fields = "__all__"

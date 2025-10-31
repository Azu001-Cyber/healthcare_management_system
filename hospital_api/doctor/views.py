from rest_framework import generics, permissions
from .models import Doctor, Nurse
from .serializers import DoctorSerializer, NurseSerializer


# Create your views here.

class DoctorProfileView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    


class DoctorDeleteProfileView(generics.DestroyAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated & permissions.IsAdminUser]

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()



class NurseProfileView(generics.RetrieveUpdateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    


class NurseDeleteProfileView(generics.DestroyAPIView):

    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [permissions.IsAuthenticated & permissions.IsAdminUser]

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
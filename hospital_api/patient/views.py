from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientProfileView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    

class PatientDeleteProfileView(generics.DestroyAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated & permissions.IsAdminUser]

    def get_object(self):
        return self.queryset.get(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
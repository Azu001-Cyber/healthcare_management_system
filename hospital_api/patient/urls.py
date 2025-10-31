from django.urls import path
from .views import PatientProfileView, PatientDeleteProfileView

urlpatterns = [
    path('profile/', PatientProfileView.as_view(), name='patient-profile'),
    path('profile/delete/', PatientDeleteProfileView.as_view(), name='delete-patient-profile')
]

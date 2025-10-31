from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.DoctorProfileView.as_view(), name='doctor-profile'),
    path('profile/delete/', views.DoctorDeleteProfileView.as_view(), name='delete-doctor-profile'),
    path('profile/', views.NurseProfileView.as_view(), name='nurse-profile'),
    path('profile/delete/', views.NurseDeleteProfileView.as_view(), name='delete-nurse-profile'),
]
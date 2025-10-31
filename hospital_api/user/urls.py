
from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView,
                                            TokenVerifyView,
                                            TokenObtainPairView)
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', views.register, name='Register'),
    path('api/login/', views.login, name='login'),
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
]




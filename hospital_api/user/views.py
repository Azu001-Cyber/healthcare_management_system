from django.shortcuts import render
from user.serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import (ListModelMixin,
#                                     CreateModelMixin,
#                                     RetrieveModelMixin, 
#                                     DestroyModelMixin)
# Create your views here.

# class CreateUser(GenericAPIView, CreateModelMixin):
#     class Meta:
#         Model = CustomUser
#         serializer_class = CustomUserSerializer
    
#     def post(self, request, *args, **kwargs):
#         # serializer = 
#         return Response()

class TenPerDayUserThrottle(UserRateThrottle):
    rate = '10/day'

@api_view(['GET', 'POST'])
@throttle_classes(TenPerDayUserThrottle)
def register(request):
    if request.method == 'POST':
        serializer  = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response({
                'message' : 'User registered successfully!',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED);
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@throttle_classes(TenPerDayUserThrottle)
def login(request):
     ...
    
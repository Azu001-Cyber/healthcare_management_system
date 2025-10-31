from django.shortcuts import render
from django.contrib.auth import authenticate
from user.serializers import CustomUserSerializer
from rest_framework.decorators import (api_view,
                                    APIView)

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
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
def login(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {"message":"Login Successful!",
                    "refresh":str(refresh),
                    "access":str(refresh.access_token)
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {'error':'Invalid username or password'
                },
                status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
        


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try: 
            refresh_token = request.data.get('refresh')
            if refresh_token is None:
                return Response(
                    {
                        "error":"Refresh token is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'message':"Logout Successful",
            },
            status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response({
                "error":'Invalide or expired token'
            },
            status=status.HTTP_400_BAD_REQUEST
            )


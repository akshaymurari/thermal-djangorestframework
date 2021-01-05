from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from rest_framework.permissions import IsAdminUser,BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

class savedet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

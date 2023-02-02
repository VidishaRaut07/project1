from django.shortcuts import render
from .serializers import AuthSerializers
from rest_framework.generics import CreateAPIView

# Create your views here.
class AuthView(CreateAPIView):
    serializer_class = AuthSerializers

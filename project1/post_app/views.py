from django.shortcuts import render
from .serializers import PostSerializers, Post
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .custompermission import IsOwnerOrReadOnlyOrCreate

# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnlyOrCreate]





    
    


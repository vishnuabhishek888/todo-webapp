from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .models import *
from .serializers import *
# Create your views here.

class ListToDo(generics.ListAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDo(generics.DestroyAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    CRUD para modelo Task. Las operaciones CRUD las crea automátizamente
    DRF al utilizar "ModelViewSet"
    """
    queryset = Task.objects.all().order_by('-created_at')  # Ordenar por fecha descendente con la sintaxis del ORM.
    serializer_class = TaskSerializer  # Asociar el serializer creado
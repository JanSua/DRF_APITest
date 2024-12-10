"""
El serializador es para convertir datos de modelos
en formatos conocidos como JSON o XML para la API
"""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer): # Hereda de serializers.ModelSerializer, es propio de DRF
    """
    Serializer para el modelo Task.
    Convierte el modelo en JSON y viceversa.
    """
    class Meta:
        model = Task  # Modelo de origen
        fields = ['id', 'title', 'description', 'is_completed', 'created_at']  # Campos que se expondrán en la API

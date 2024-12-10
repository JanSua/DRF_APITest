from django.db import models


class Task(models.Model):
    # Modelo básico de una tarea
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Descripción
    is_completed = models.BooleanField(default=False)  # Estado
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.title

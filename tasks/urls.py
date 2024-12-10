from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Crear un router
router = DefaultRouter() # es propio de DRF, genera auto. las rutas para el ViewSet.
router.register(r'tasks', TaskViewSet)  # Registrar el ViewSet con el router (ruta /tasks/)

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas generadas por el router
]

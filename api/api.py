from rest_framework import viewsets, permissions
from .models import Empleados
from api.serializers import EmpleadoSerializers


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializers
from rest_framework.viewsets import ModelViewSet
from .models import ChecklistMaquinaria
from .serializers import ChecklistSerializer

class ChecklistViewSet(ModelViewSet):
    """
    Controlador de la API.
    Permite realizar operaciones CRUD:
    Crear, Leer, Actualizar y Eliminar checklists.
    """

    queryset = ChecklistMaquinaria.objects.all()
    serializer_class = ChecklistSerializer

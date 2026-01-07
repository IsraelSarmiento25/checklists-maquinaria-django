from rest_framework.viewsets import ModelViewSet
from .models import Tractor, Operador, ChecklistMaquinaria
from .serializers import TractorSerializer, OperadorSerializer, ChecklistSerializer


class TractorViewSet(ModelViewSet):
    queryset = Tractor.objects.all()
    serializer_class = TractorSerializer


class OperadorViewSet(ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer


class ChecklistViewSet(ModelViewSet):
    queryset = ChecklistMaquinaria.objects.all()
    serializer_class = ChecklistSerializer

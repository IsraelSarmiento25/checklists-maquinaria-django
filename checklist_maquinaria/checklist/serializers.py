from rest_framework import serializers
from .models import ChecklistMaquinaria

class ChecklistSerializer(serializers.ModelSerializer):
    """
    Convierte el modelo ChecklistMaquinaria en JSON
    y valida los datos recibidos desde Insomnia.
    """

    class Meta:
        model = ChecklistMaquinaria
        fields = '__all__'

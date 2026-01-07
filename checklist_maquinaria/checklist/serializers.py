from rest_framework import serializers
from .models import Tractor, Operador, ChecklistMaquinaria


class TractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tractor
        fields = '__all__'


class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = '__all__'


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistMaquinaria
        fields = '__all__'
from django.db import models


class Tractor(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=50, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.modelo}"


class Operador(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class ChecklistMaquinaria(models.Model):
    tractor = models.ForeignKey(
        "Tractor",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    operador = models.ForeignKey(
        "Operador",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    fecha = models.DateField(auto_now_add=True)

    motor = models.BooleanField(default=False)
    transmision = models.BooleanField(default=False)
    frenos = models.BooleanField(default=False)

    sistema_electrico = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)

    llantas = models.BooleanField(default=False)
    fugas = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Mantenimiento {self.tractor} - {self.fecha}"

from django.db import models

class ChecklistMaquinaria(models.Model):
    """
    Este modelo representa una revisión de maquinaria.
    Cada campo corresponde a un punto del checklist.
    """

    nombre_maquinaria = models.CharField(
        max_length=100,
        help_text="Nombre o código de la maquinaria"
    )

    operador = models.CharField(
        max_length=100,
        help_text="Nombre del operador que realiza la inspección"
    )

    fecha = models.DateField(
        auto_now_add=True,
        help_text="Fecha automática de la revisión"
    )

    # ÁREA MECÁNICA
    motor = models.BooleanField(default=False)
    transmision = models.BooleanField(default=False)
    frenos = models.BooleanField(default=False)

    # SISTEMA ELÉCTRICO
    sistema_electrico = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)

    # CONDICIONES GENERALES
    llantas = models.BooleanField(default=False)
    fugas = models.BooleanField(default=False)

    observaciones = models.TextField(
        blank=True,
        help_text="Comentarios adicionales"
    )

    def __str__(self):
        return f"{self.nombre_maquinaria} - {self.fecha}"

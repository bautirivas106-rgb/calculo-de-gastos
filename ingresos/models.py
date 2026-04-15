from django.db import models

class Ingreso(models.Model):
    TIPO_INGRESO_CHOICES = [
        ('sueldo', 'Sueldo'),
        ('propina', 'Propina'),
        ('extra', 'Otro Ingreso'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_INGRESO_CHOICES, verbose_name="Tipo de Ingreso")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto ($)")
    fecha = models.DateField(verbose_name="Fecha")
    descripcion = models.CharField(max_length=200, blank=True, null=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Sueldos y Propinas"

    def __str__(self):
        return f"{self.get_tipo_display()} - ${self.monto}"

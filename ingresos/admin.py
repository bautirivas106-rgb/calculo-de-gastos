from django.contrib import admin
from .models import Ingreso

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo', 'monto', 'descripcion')
    list_filter = ('tipo', 'fecha')

# Register your models here.

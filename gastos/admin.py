from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo', 'monto')
    list_filter = ('tipo', 'fecha')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('fecha', 'monto', 'tipo')
        }),
        ('Detalle Hogar', {
            'fields': ('sub_hogar',),
        }),
        ('Detalle Gasto Boludo', {
            'fields': ('sub_boludo', 'tipo_plataforma', 'servicio_especifico'),
        }),
        ('Extras', {
            'fields': ('descripcion',),
        }),
    )
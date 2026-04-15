from django.apps import AppConfig

class GastosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gastos'  # Nombre técnico (debe coincidir con la carpeta)
    verbose_name = 'Mis Gastos' # Nombre visual que verás en el panel azul
from django.db import models

class Gasto(models.Model):
    # --- OPCIONES PARA GASTOS ---
    TIPO_CHOICES = [
        ('hogar', 'Gasto de Hogar'),
        ('boludo', 'Gasto Boludo'),
        ('amigos', 'Salida con Amigos'),
        ('pareja', 'Salida con mi Pareja'),
    ]

    SUB_HOGAR_CHOICES = [
        ('alquiler', 'Alquiler'),
        ('wifi', 'WiFi'),
        ('luz', 'Luz'),
        ('gas', 'Gas'),
        ('agua', 'Agua'),
        ('expensas', 'Expensas'),
        ('compras_casa', 'Compras de casa'),
    ]

    SUB_BOLUDO_CHOICES = [
        ('golosinas', 'Golosinas'),
        ('gaseosas', 'Gaseosas'),
        ('cigarrillos', 'Cigarrillos'),
        ('galletitas', 'Galletitas'),
        ('plataformas', 'Plataformas Digitales'),
    ]

    TIPO_PLATAFORMA_CHOICES = [
        ('peliculas', 'Películas y Series'),
        ('musica', 'Música'),
        ('tv_deportes', 'TV en vivo y Deportes'),
        ('videojuegos', 'Videojuegos'),
    ]

    SERVICIO_CHOICES = [
        # Películas
        ('netflix', 'Netflix'), ('disney', 'Disney+'), ('max', 'Max'), ('prime', 'Amazon Prime Video'),
        ('paramount', 'Paramount+'), ('apple_tv', 'Apple TV+'), ('star', 'Star+'), ('claro', 'Claro Video'), ('mubi', 'MUBI'),
        # Música
        ('spotify', 'Spotify'), ('apple_music', 'Apple Music'), ('yt_music', 'YouTube Music'), ('deezer', 'Deezer'),
        # TV y Deportes
        ('dgo', 'DGO'), ('flow', 'Flow'), ('tyc', 'TyC Sports Play'), ('basquet', 'Básquet Pass'), ('nba', 'NBA League Pass'),
        # Videojuegos
        ('xbox', 'Xbox Game Pass'), ('ps_plus', 'PlayStation Plus'), ('nintendo', 'Nintendo Switch Online'),
    ]

    # --- CAMPOS DEL MODELO GASTO ---
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Categoría Principal")
    
    # Campos condicionales
    sub_hogar = models.CharField(max_length=20, choices=SUB_HOGAR_CHOICES, blank=True, null=True, verbose_name="Detalle Hogar")
    sub_boludo = models.CharField(max_length=20, choices=SUB_BOLUDO_CHOICES, blank=True, null=True, verbose_name="Detalle Gasto Boludo")
    tipo_plataforma = models.CharField(max_length=20, choices=TIPO_PLATAFORMA_CHOICES, blank=True, null=True, verbose_name="Tipo de Plataforma")
    servicio_especifico = models.CharField(max_length=25, choices=SERVICIO_CHOICES, blank=True, null=True, verbose_name="Servicio Específico")
    
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto ($)")
    fecha = models.DateField(verbose_name="Fecha del Gasto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Observaciones / Detalle")

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Mis Gastos"

    def __str__(self):
        return f"{self.get_tipo_display()} - ${self.monto}"
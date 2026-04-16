from django.db import models

class Solicitud(models.Model):

    OPCIONES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre = models.CharField(max_length=150, verbose_name="Nombre del solicitante")
    documento = models.CharField(max_length=50, verbose_name="Documento de identidad")
    correo = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.IntegerField(verbose_name="Teléfono de contacto")
    tipo = models.CharField(max_length=20, choices=OPCIONES, verbose_name="Tipo de solicitud")
    asunto = models.CharField(max_length=100, verbose_name="Asunto")
    descripcion = models.TextField(verbose_name="Descripción detallada")
    fecha = models.DateField(verbose_name="Fecha de la solicitud")
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True, verbose_name="Archivo adjunto")

    def __str__(self):
        return self.nombre
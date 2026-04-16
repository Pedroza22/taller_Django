from django.db import models

class Solicitud(models.Model):

    OPCIONES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre = models.CharField(max_length=150)
    documento = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=OPCIONES)
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
from django.contrib import admin
from .models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'correo', 'tipo', 'fecha')
    search_fields = ('nombre', 'documento', 'correo')
    list_filter = ('tipo', 'fecha')

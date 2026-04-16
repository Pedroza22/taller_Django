from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.formulario_solicitud, name='formulario_solicitud'),
    path('ok/', views.confirmacion_solicitud, name='confirmacion_solicitud'),
]
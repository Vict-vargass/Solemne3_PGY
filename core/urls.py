from django.urls import path
from .views import home, formulario, registroUsuarios, solicitudes,add_obra

urlpatterns = [
    path('', home, name="inicio"),
    path('formulario-contacto/', formulario, name='contacto'),
    path('registro/', registroUsuarios, name='registro'),
    path('solicitudes/', solicitudes, name='solicitud'),
    path('agregar-obra/', add_obra, name='agregar'),
]
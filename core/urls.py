from django.urls import path
from .views import home, formulario, registroUsuarios

urlpatterns = [
    path('', home, name="inicio"),
    path('formulario-contacto/', formulario, name='contacto'),
    path('registro/', registroUsuarios, name='registro')
]
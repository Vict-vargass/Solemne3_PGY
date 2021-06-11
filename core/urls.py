from django.urls import path
from .views import home, formulario

urlpatterns = [
    path('', home, name="inicio"),
    path('formulario-contacto/', formulario, name='contacto'),
]
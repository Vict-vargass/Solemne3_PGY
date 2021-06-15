from django import forms
from django import forms
from django.db.models.fields import EmailField
from django.forms import ModelForm
from .models import usuarios


class registroUsuario (ModelForm):

    class Meta:
        model = usuarios
        fields=['nombreUsuario','emailUsuario','contraseñaUsuario']


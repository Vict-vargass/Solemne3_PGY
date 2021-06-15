from django import forms
from django.db.models.fields import CharField, EmailField
from django.forms import ModelForm, widgets
from .models import usuarios

class registroUsuario (forms.ModelForm):

    class Meta:
        model = usuarios
        fields=['nombreUsuario','emailUsuario', 'contraseñaUsuario']
        label={
            'nombreUsuario': 'Nombre',
            'emailUsuario': 'Correo electronico',
            'contraseñaUsuario': 'Contraseña'
        }
        widgets={
            'nombreUsuario': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'}),
            'emailUsuario': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su correo'}),
            'contraseñaUsuario': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese su contraseña'})
        }
from django import forms
from django.db.models import fields
from django.db.models.fields import CharField, EmailField
from django.forms import ModelForm, widgets
from .models import usuarios, solicitudesContacto, solicitudObra

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


class formularioContacto (forms.ModelForm):
    class Meta:
        model = solicitudesContacto
        fields = ['nombreSolicitante','correo','run','pasaporte','celular','ciudad','mensaje']
        widgets={
            'nombreSolicitante': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'}),
            'correo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su correo'}),
            'run': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su run'}),
            'pasaporte': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su pasaporte'}),
            'celular': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su celular'}),
            'ciudad': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Ingrese su ciudad'}),
            'mensaje' : forms.Textarea(attrs={'class':'form-control','placeholder':'motivo de contacto'})
        }


class publicarObra(forms.ModelForm):

    class Meta:
        model = solicitudObra
        fields = ['nombreObra','historia','descripcion','precio','tecnicaUsada','categoria']
        widgets={
            'nombreObra': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la obra'}),
            'historia' : forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese la historia de la obra'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese una descripción'}),
            'tecnicaUsada' : forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese la tecnica empleada'})
        }
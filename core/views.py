from django.shortcuts import render
from .forms import registroUsuario

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def registroUsuarios(request):
    datos={'form': registroUsuario()}
    if request.method == 'POST':
        registo_usuario = registroUsuario(request.POST)
        if registo_usuario.is_valid:
            registo_usuario.save()
    return render(request, 'core/registro.html', datos)
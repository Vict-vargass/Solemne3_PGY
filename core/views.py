from core.models import solicitudObra
from django.shortcuts import redirect, render
from .forms import registroUsuario, publicarObra, EditarObra
from .models import solicitudObra

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

def solicitudes(request):
    solicitud_obra = solicitudObra.objects.all()
    datos = {
        'solicitud': solicitud_obra
    }
    return render(request, 'core/solicitudesObras.html', datos)

def add_obra(request):
    datos = {
        'form': publicarObra() 
        }
    if request.method == 'POST':
        formulario_add = publicarObra(request.POST)
        if formulario_add.is_valid:
            formulario_add.save()

    return render(request, 'core/crearSolicitudObra.html', datos)


def edit_obra(request, pk):
    obra = solicitudObra.objects.get(idSolicitudObra = pk)
    datos = {
        'form': EditarObra(instance= obra) 
        }
    if request.method == 'POST':
        formulario_edit = EditarObra(data=request.POST, instance= obra)
        if formulario_edit.is_valid:
            formulario_edit.save()
    return render(request, 'core/editarSolicitud.html', datos)


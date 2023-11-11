from django.shortcuts import render, redirect, get_object_or_404
from templates import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, AddPymeForm, Login
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Pymes, Solicitudes, Propietarios
from django.contrib.auth.views import LoginView

# Create your views here.


def main(request):
    pymes = Pymes.objects.all()
    if request.user.is_authenticated:
        user = request.user.rol
        data = { "u":user, "pymes":pymes}
        return render(request, "mainPage/main.html", data)
    else:
        data = { "pymes":pymes}
        return render(request, "mainPage/main.html", data)


def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} Registrado')
            return redirect('main:main')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'mainPage/register.html', context)



def cuentaUser(request):
    if request.user.is_authenticated:
        nameUser = request.user.first_name
        lastName = request.user.last_name
        email = request.user.email
        data = {"nombre": nameUser,"apellido": lastName , "email":email}
        return render(request, 'mainPage/users.html', data)
    else:
        
        return redirect('main:login')
    


def generar_nombre_unico(nombre_original):
    import uuid
    extension = nombre_original.split('.')[-1]
    nombre_unico = f"{uuid.uuid4().hex}.{extension}"
    return nombre_unico
    
def solicitud(request):
    if request.method == 'POST':
        form = AddPymeForm(request.POST, request.FILES)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            fecha_solicitud = request.POST.get('fecha_de_solicitud')
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            rut = request.POST.get('rut')
            categoria = request.POST.get('categoria')
            nombre_pyme = request.POST.get('nombrePyme')
            solicitud = request.POST.get('solicitud')
            imagen = request.FILES.get('imagen')
            idUser = request.user.id
            s = Solicitudes(fecha_de_solicitud=fecha_solicitud, nombre=nombre, apellidos=apellidos, 
                                      rut=rut, categoria=categoria, nombrePyme=nombre_pyme, solicitud=solicitud,
                                      imagen=imagen, idSolicitante=idUser)
            s.save()
            messages.success(request, f'Solicitud Enviada')
            return redirect('main:main')
        
    else:
        form = AddPymeForm()
    context = {'form': form}
    return render(request, 'mainPage/add-pyme.html', context)


def solicitudAdmin(request):
    soli = Solicitudes.objects.all()
    data = {'solicitudes':soli,}
    return render(request, "mainPage/solicitudes.html", data)

def rechazar(request,pk):
    soli = get_object_or_404(Solicitudes, pk=pk)
    soli.delete()
    return redirect("main:solicitudAdmin")


def aceptar(request,pk):
    
    soli = get_object_or_404(Solicitudes, pk=pk)
    if request.user.is_authenticated:
        guardarUsuario = Propietarios(nombrePyme = soli.nombrePyme, datosPropietario_id = soli.idSolicitante)
        guardarUsuario.save()
        usuario = get_object_or_404(Usuarios, id=soli.idSolicitante)
        rolAdmin = 2
        usuario.rol = rolAdmin
        usuario.save()
        guardar = Pymes(nombrePyme=soli.nombrePyme, categoria=soli.categoria, imagen=soli.imagen, propietario_id = guardarUsuario.id)
        guardar.save()
        soli.delete()
        return redirect("main:solicitudAdmin")


def soliDetalles(request, pk):
    solicitudes = get_object_or_404(Solicitudes, pk=pk)
   
    return render(request, "mainPage/detallesSolicitudes.html", {'soli': solicitudes})


class login(LoginView):
    form_class = Login 
    template_name = 'mainPage/login.html'  

    # agregar lógica personalizada para el inicio de sesión
    def form_valid(self, form):
        # Realizar acciones personalizadas aquí si el formulario es válido
        return super().form_valid(form)

    def form_invalid(self, form):
        # Realizar acciones personalizadas aquí si el formulario es inválido
        return super().form_invalid(form)
    
    


def error404(request, exception):
    return render(request, '/error404.html', status=404)
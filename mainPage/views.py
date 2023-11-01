from django.shortcuts import render, redirect, get_object_or_404
from templates import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, AddPymeForm
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Pymes, Solicitudes

# Create your views here.


def main(request):
    pymes = Pymes.objects.all()
    data = {"img":"imagenes\logo_pyme.jpg"}
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
    
    

def solicitud(request):
    if request.method == 'POST':
        form = AddPymeForm(request.POST, request.FILES)
        if form.is_valid():
            soli = form.save()
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



def soliDetalles(request, pk):
    solicitudes = get_object_or_404(Solicitudes, pk=pk)
   
    return render(request, "mainPage/detallesSolicitudes.html", {'soli': solicitudes})
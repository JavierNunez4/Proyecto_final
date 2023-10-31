from django.shortcuts import render, redirect
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
            return redirect('main')
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
        
        return redirect('login')
    
    

def solicitud(request):
    if request.method == 'POST':
        form = AddPymeForm(request.POST, request.FILES)
        if form.is_valid():
            soli = form.save()
            messages.success(request, f'Solicitud Enviada')
            return redirect('main')
        
    else:
        form = AddPymeForm()
    context = {'form': form}
    return render(request, 'mainPage/add-pyme.html', context)


def solicitudAdmin(request):
    soli = Solicitudes.objects.all()
    data = {'solicitudes':soli,}
    return render(request, "mainPage/solicitudes.html", data)
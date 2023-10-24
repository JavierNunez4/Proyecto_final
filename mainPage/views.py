from django.shortcuts import render, redirect
from templates import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Usuarios

# Create your views here.


def main(request):
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
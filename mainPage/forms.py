from django import forms
from .models import Usuarios, Solicitudes
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = Usuarios
        fields = ['first_name','last_name',  'email', 'username',  ] 
        help_texts = {k:"" for k in fields}


class AddPymeForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    apellidos = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    nombrePyme = forms.CharField(label='Nombre de su Pyme', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    solicitud = forms.CharField(label='Descripcion de solicitud' ,widget=forms.Textarea(attrs={"class":"form-control"}), max_length=250)
    imagen = forms.ImageField(label="Logo de su Pyme", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Solicitudes
        fields = ['id','nombre','apellidos',  'nombrePyme', 'solicitud', 'imagen'] 
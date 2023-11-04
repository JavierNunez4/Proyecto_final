from django import forms
from .models import Usuarios, Solicitudes
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Ingrese su Email"}))
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingrese su Nombre de Usuario"}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su Nombre"}))
    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingrese su Apellido"}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingrese su Contraseña"}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Repetir Contraseña"}))
    
    class Meta:
        model = Usuarios
        fields = ['username','first_name','last_name',  'email', ] 
        help_texts = {k:"" for k in fields}


class AddPymeForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    apellidos = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    rut = forms.CharField(label='Rut Empresa', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=9)
    nombrePyme = forms.CharField(label='Nombre de su Pyme', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    categoria = forms.CharField(label='Categoria de su Pyme', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    solicitud = forms.CharField(label='Descripcion de solicitud' ,widget=forms.Textarea(attrs={"class":"form-control"}), max_length=250)
    imagen = forms.ImageField(label="Logo de su Pyme", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Solicitudes
        fields = ['id','nombre','apellidos','rut',  'nombrePyme', 'categoria','solicitud', 'imagen'] 
        
        
class Login(AuthenticationForm):
    username = forms.CharField(label='Nombre de Usuario',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingrese su Nombre de Usuario"}), max_length=15)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingrese su Contraseña"}))
    
    class Meta:
        
        fields = ['username','password'] 
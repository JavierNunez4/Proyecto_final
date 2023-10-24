from django import forms
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = Usuarios
        fields = ['first_name','last_name',  'email', 'username',  ] 
        help_texts = {k:"" for k in fields}

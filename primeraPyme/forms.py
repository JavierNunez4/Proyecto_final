from django import forms
from mainPage.models import Productos


class ProductoFrom(forms.ModelForm):
    nombreProducto = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), max_length=35)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}), max_length=250)
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control"}), max_digits=10, decimal_places=2)
    imagen = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Productos
        fields = ['id', 'pymeAsociada', 'nombreProducto', 'descripcion','cantidad', 'precio', 'imagen' ]
        

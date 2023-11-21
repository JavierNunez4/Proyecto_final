from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoFrom
from django.views.generic import View
from django.http import HttpResponseRedirect
from mainPage.models import Productos, Propietarios, Pymes
from django.urls import reverse



# Create your views here.

#vista principal de la pyme
def pyme1(request, pk):
    pyme = get_object_or_404(Pymes, pk=pk)
    propietario = Propietarios.objects.all()
    productos = Productos.objects.all()
    data = { 'productos':productos, "pyme":pyme, "propie":propietario}
    return render(request, "primeraPyme/snakedreams.html",data)


#funcion basa en clases que permite mostrar y guardar el formulario para agregar productos
class GuardarProducto(View):
    def get(self, request, pk):
        pyme = get_object_or_404(Pymes, pk = pk)
        form = ProductoFrom()
        return render(request, "primeraPyme/add-producto.html", {
            "form": form
        })
        
        
        
    def post(self, request, pk):
        form = ProductoFrom(request.POST, request.FILES)
        
        if request.user.is_authenticated:
            userRol = request.user.rol
            pyme = get_object_or_404(Pymes, pk=pk)
            
            if form.is_valid():
                nombre = form.cleaned_data['nombreProducto']
                descripcion = form.cleaned_data['descripcion']
                cantidad = form.cleaned_data['cantidad']
                precio = form.cleaned_data['precio']
                imagen = form.cleaned_data['imagen']
                
                product = Productos(
                    nombreProducto=nombre,
                    descripcion=descripcion,
                    cantidad=cantidad, 
                    precio=precio, 
                    imagen=imagen,
                    pymeAsociada=pyme  # Asociamos directamente la instancia de Pymes
                )
                product.save()
                return redirect('main:main')
            
            # Si el formulario no es válido, manejar el caso
            data = {"user": userRol, "pyme": pyme, "form": form}
            return render(request, "primeraPyme/snakedreams.html", data)
        
        
#detalles de cada producto
def detalles(request, pk):
    pyme = Pymes.objects.all()
    producto = get_object_or_404(Productos, pk=pk)
    data = {'producto': producto, "pyme":pyme }
    return render(request, "primeraPyme/producto.html", data)


# carrito de compras 


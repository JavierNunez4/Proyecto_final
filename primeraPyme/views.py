from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoFrom
from django.views.generic import View
from django.http import HttpResponseRedirect
from mainPage.models import Productos, Propietarios, Pymes
from django.urls import reverse


# Create your views here.


def pyme1(request):
    productos = Productos.objects.all()
    data = {"img":"imagenes\logo_pyme.jpg", 'productos':productos}
    return render(request, "primeraPyme/snakedreams.html",data)



class GuardarProducto(View):
    def get(self, request):
        form = ProductoFrom()
        return render(request, "primeraPyme/add-producto.html", {
            "form": form
        })
        
        
        
    def post(self, request):
        form = ProductoFrom(request.POST, request.FILES)
        py = Pymes.objects.all()
        p = Propietarios.objects.all()
        if request.user.is_authenticated:
            userRol = request.user.rol
            if form.is_valid():
                form.save()
                return redirect('gestion:pyme1')
            data = {"user":userRol}
            return render(request, "primeraPyme/snakedreams.html", data)
        
        
    
        
        


def detalles(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    return render(request, "primeraPyme/producto.html", {'producto': producto})
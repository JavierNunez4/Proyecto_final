from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoFrom
from django.views.generic import View
from django.http import HttpResponseRedirect
from mainPage.models import Productos
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
        if form.is_valid():
            form.save()
            return redirect('gestion:pyme1')
        
        


def detalles(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
   
    return render(request, "primeraPyme/producto.html", {'producto': producto})
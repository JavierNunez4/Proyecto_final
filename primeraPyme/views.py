from django.shortcuts import render
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
            return HttpResponseRedirect(reverse('pyme1'))
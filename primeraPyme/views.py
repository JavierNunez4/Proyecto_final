from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import ProductoFrom
from django.views.generic import View
from django.http import HttpResponseRedirect
from mainPage.models import Usuarios,ItemPedido,Pedido,Productos, Propietarios, Pymes
from django.urls import reverse
from carro.carro import Carro
from carro.context_processor import total_carrito



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

def pedidos(request):
    
    total_carro = total_carrito(request)["total_carro"]
    contexto = {
        # Otros elementos del contexto
        'total_carro': total_carro,
    }
    return render(request, "primeraPyme/pedido.html", contexto)

def agregarCarro(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id =producto_id)
    carro.agregar(producto)
    return redirect("main:main")

def eliminarCarro(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id =producto_id)
    carro.remove(producto)
    return redirect("main:main")


def restarCarro(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id =producto_id)
    carro.decrement(producto)
    return redirect("main:main")

def vaciarCarro(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect("main:main")

def agregarPedido(request):
    carro = Carro(request)
# Recorrer la lista de productos en el carrito
    if request.user.is_authenticated:
        productos_en_carro = carro.carro.values()
        userid = request.user.id
        user = Usuarios.objects.get(id=userid)
        pedido = Pedido(usuario = user, 
                                total =0)
        if productos_en_carro:  
            for producto in productos_en_carro:
                idProducto = producto["producto_id"]
                produ = Productos.objects.get(id=idProducto)
                cantidad = producto["cantidad"]
                
                
                detailPedido = ItemPedido(pedido = pedido,
                                cantidad = cantidad,
                                producto = produ)
                pedido.save()
                detailPedido.save()
            return redirect("main:main")
        
    
def detallePedido(request):
    if request.user.is_authenticated:
        pedidos = Pedido.objects.all()
        data = {"pedidos":pedidos}
        return render(request, "primeraPyme/pedido-usuario.html", data)
    else:
        return render(request, "primeraPyme/pedido-usuario.html")
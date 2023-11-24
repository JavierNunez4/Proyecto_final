from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuarios(AbstractUser):
    rol = models.IntegerField(default=1) # 1 para usuarios 2 para propietarios y 3 para administradores
    
    class Meta:    
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='usuarios'
    


class Propietarios(models.Model):
    datosPropietario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombrePyme = models.CharField(max_length=30)
        
        
    class Meta:
        verbose_name='Propietario'
        verbose_name_plural='Propietarios'
        db_table='propietarios'


    
class Solicitudes(models.Model):
    
    fecha_de_solicitud = models.DateField(auto_now_add=True, null=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    categoria = models.CharField(max_length=60, default=None)
    nombrePyme = models.CharField(max_length=100)
    solicitud = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='logoPymesSoli', null=True)
    idSolicitante = models.IntegerField(null=True, default=None)
    
    class Meta:
        verbose_name='Solicitud'
        verbose_name_plural='Solicitudes'
        db_table='solicitudes'

class Pymes(models.Model):
    
    nombrePyme=models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20)
    propietario= models.ForeignKey(Propietarios,null=True,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='logoPymes', null=True)
    
    def get_img_url(self):
        return self.logo.imagen.url
    
    class Meta:
        verbose_name='Pymes'
        verbose_name_plural='Pymes'
        db_table='pymes'
    



class Productos(models.Model):
    
    pymeAsociada= models.ForeignKey(Pymes,null=True, blank=True, on_delete=models.CASCADE)
    nombreProducto=models.CharField(max_length=35)
    descripcion=models.CharField(max_length=150)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    cantidad=models.IntegerField()
    imagen = models.ImageField(upload_to='imagenesT', null=True)
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        db_table='productos'
    
    
    
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Productos, through='ItemPedido')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    
    
    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        db_table='pedidos'

    def __str__(self):
        return f"Pedido de {self.usuario.username} - {self.creado_en}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.pedido}"
    
    class Meta:
        verbose_name='Detalle_Pedido'
        verbose_name_plural='Detalle_Pedidos'
        db_table='pedidos_detalle'
    
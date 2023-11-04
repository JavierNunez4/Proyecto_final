from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuarios(AbstractUser):
    
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
    rut = models.IntegerField(default=0)
    categoria = models.CharField(max_length=60, default=None)
    nombrePyme = models.CharField(max_length=100)
    solicitud = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='logoPymesSoli', null=True)
    
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
    precio=models.FloatField()
    imagen = models.ImageField(upload_to='imagenesT', null=True )
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        db_table='productos'
    
    

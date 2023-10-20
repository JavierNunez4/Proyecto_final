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
    

class Pymes(models.Model):
    
    nombrePyme=models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20)
    propietario= models.ForeignKey(Propietarios,null=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Pymes'
        verbose_name_plural='Pymes'
        db_table='pymes'
    



class Productos(models.Model):
    
    pymeAsociada= models.ForeignKey(Pymes,null=True, blank=True, on_delete=models.RESTRICT)
    nombreProducto=models.CharField(max_length=35)
    descripcion=models.CharField(max_length=50)
    precio=models.FloatField()
    imagen = models.ImageField(upload_to='imagenes', null=True )
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        db_table='productos'
    
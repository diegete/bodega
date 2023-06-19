from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from pytz import timezone as pytz_timezone
# Create your models here.
class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,max_length=20,verbose_name='idProducto')
    nombre = models.CharField(max_length=25,verbose_name='Nombre producto')
    stock = models.IntegerField(verbose_name='stock')
    categoria= models.CharField(max_length=20,verbose_name='Categoria')
    imagen = models.URLField(verbose_name='foto',null=True,blank='true')
    precio = models.CharField(max_length=6,verbose_name='precio',default=False)
    estado = models.BooleanField(verbose_name='estado',default=False)
    fecha = models.DateTimeField(default=now)
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering=['nombre']

    def __str__(self) -> str:
        return self.idProducto+' '+self.nombre


class Carrito(models.Model):
    fecha = models.DateTimeField(default=now)
    productos = models.JSONField(default=list)

    @classmethod
    def crear_carrito(cls, registros):
        carrito = cls()
        carrito.productos = registros
        
        carrito.save()
        return carrito

     
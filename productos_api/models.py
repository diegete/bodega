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

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering=['nombre']

    def __str__(self) -> str:
        return self.idProducto+' '+self.nombre


class Carrito(models.Model):
    fecha = models.DateTimeField(default=now)
    productos = models.JSONField(default=list)
    def save(self, *args, **kwargs):
        clt_timezone = pytz_timezone("Chile/Continental")
        self.fecha = self.fecha.astimezone(clt_timezone)
        super().save(*args, **kwargs)  

    class Meta:
        verbose_name='Carrito'
        verbose_name_plural='Ordenes'
        ordering=['id']

    @classmethod
    def crear_carrito(cls, registros, *args, **kwargs):
        carrito = cls()
        carrito.productos = registros

        # Obtener la fecha y hora actual en GMT
        fecha_gmt = timezone.now()

        # Convertir la fecha y hora a GMT-5 (restar 5 horas)
        fecha_gmt_menos_4 = fecha_gmt - timezone.timedelta(hours=4)

        # Asignar la fecha y hora convertida al carrito
        carrito.fecha = fecha_gmt_menos_4

        carrito.save()
        return carrito

     
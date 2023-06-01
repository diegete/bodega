from django.db import models

# Create your models here.
class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,max_length=20,verbose_name='idProducto')
    nombre = models.CharField(max_length=25,verbose_name='Nombre producto')
    stock = models.CharField(max_length=6,verbose_name='stock')
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


    
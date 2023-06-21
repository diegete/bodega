from django.db import models
from django.utils.timezone import now

class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=20, verbose_name='ID Producto')
    nombre = models.CharField(max_length=25, verbose_name='Nombre producto')
    stock = models.IntegerField(verbose_name='Stock')
    categoria = models.CharField(max_length=20, verbose_name='Categoría')
    imagen = models.URLField(verbose_name='Foto', null=True, blank=True)
    precio = models.CharField(max_length=6, verbose_name='Precio')
    estado = models.BooleanField(verbose_name='Estado')
    fecha = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.id} - {self.nombre}"

class Carrito(models.Model):
    fecha = models.DateTimeField(default=now)
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    direccion = models.CharField(max_length=30, verbose_name='Dirección')
    productos = models.ManyToManyField(Producto)

    def obtener_productos(self):
        return list(self.productos.values())

    def agregar_producto(self, producto):
        self.productos.add(producto)

    def quitar_producto(self, producto):
        self.productos.remove(producto)

    @classmethod
    def crear_carrito(cls, lista_productos, nombre, direccion):
        carrito = cls(nombre=nombre, direccion=direccion)
        carrito.save()
        carrito.productos.set(lista_productos)
        return carrito

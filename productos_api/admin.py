from django.contrib import admin
from .models import *

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=('idProducto','nombre','categoria','estado','imagen','stock','precio', 'fecha')

admin.site.register(Producto,ProductosAdmin)

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['productos','fecha','nombre','direccion']

admin.site.register(Carrito, CarritoAdmin)
from django.contrib import admin

from .models import Producto, Carrito

class ProductoInline(admin.TabularInline):
    model = Carrito.productos.through

class CarritoAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]
    exclude = ('productos',)
    list_display = ('nombre', 'direccion', 'fecha')

admin.site.register(Producto)
admin.site.register(Carrito, CarritoAdmin)
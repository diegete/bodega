from django.contrib import admin

from .models import CarritoProducto, Producto, Carrito

class CarritoProductoInline(admin.TabularInline):
    model = CarritoProducto
    extra = 1

class CarritoAdmin(admin.ModelAdmin):
    inlines = [CarritoProductoInline]
    exclude = ('productos',)
    list_display = ('nombre', 'direccion', 'fecha')

    def cantidad_producto(self, obj):
        return obj.carritoproducto_set.first().cantidad

    cantidad_producto.short_description = 'Cantidad'

admin.site.register(Producto)
admin.site.register(Carrito, CarritoAdmin)
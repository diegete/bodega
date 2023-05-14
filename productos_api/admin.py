from django.contrib import admin
from.models import *
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=('idProducto','nombre','categoria','estado','imagen','stock','precio')
    

admin.site.register(Producto,ProductosAdmin)
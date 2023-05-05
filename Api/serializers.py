from rest_framework import serializers
from .models import * 


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Producto
        fields = ('idProducto','nombre','categoria','stock','imagen')
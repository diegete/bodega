from rest_framework import serializers
from .models import * 


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Producto
        fields = ('id','nombre','categoria','estado','imagen','stock','precio')
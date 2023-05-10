from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import api_view

from .models import *   
from .serializers import * 

# Create your views here.

class ProductoViews(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()










# @api_view(['GET','POST','DELETE'])
# def productos_list(request):
#     if request.method == 'GET':
#          Productos=Producto.objects.all()
#          Producto_Serializer = ProductoSerializer(Productos,many=True)
#          return Response(Producto_Serializer.data)
    
#     if request.method == 'POST':
#         producto_data = JSONParser().parse(request)
#         producto_serializer = ProductoSerializer(data=producto_data)
#         if  producto_serializer.is_valid():
#              producto_serializer.save()
#              return Response(producto_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(producto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         cantidad = Producto.objects.all().delete()
#         return Response({'message':'{} han sido eliminadas de la base de datos!'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

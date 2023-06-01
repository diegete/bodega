import json
from django.shortcuts import get_object_or_404, render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
import requests as req
from .models import *   
from .serializers import * 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ProductoViews(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

def productos_api(request):
    productos = Producto.objects.all().values('idProducto','nombre','precio')
    return JsonResponse({'productos':list(productos)})

    
def home_view(request):
    return render(request, 'home.html')

def hola_mundo(resquest):
    
    url = 'http://192.168.137.1:5000/api/v1/test/saludo'
    r = req.get(url)
    respuesta =r.json()
    print(respuesta['saldo'])
    return HttpResponse(respuesta)

def user(resquest):
    
    url = 'http://192.168.137.1:5000/api/v1/test/user'
    r = req.get(url)
    respuesta =r.json()
    print(respuesta)
    return HttpResponse(respuesta)
@csrf_exempt
def agregar_a_lista(request):
    lista_productos = []
        
    if request.method == 'POST':
        
        ids_productos = request.POST.getlist('ids_productos[]')
        for id_producto in ids_productos:
            producto = get_object_or_404(Producto, pk=id_producto)
            producto_dict = {
                'idProducto':producto.idProducto,
                'nombre': producto.nombre,
                'stock': str(producto.stock),
                'categoria': producto.categoria,
                'imagen': producto.imagen,
                'precio': str(producto.precio),
                'estado': producto.estado
            }
            
            lista_productos.append(producto_dict)
    data = json.dumps(lista_productos)
    for key, value in request.POST.items():
        print(f"{key}:{value}")
    return JsonResponse(data, safe=False)


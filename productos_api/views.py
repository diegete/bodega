import json
from django.shortcuts import get_object_or_404, render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
import requests as req
from .models import *   
from .serializers import * 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

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
        try:
            data = json.loads(request.body)
            productos = data['productos']

            for producto in productos:
                id_producto = producto['id']
                cantidad = producto['cantidad']

                producto_obj = get_object_or_404(Producto, pk=id_producto)
                producto_dict = {
                    'idProducto': producto_obj.idProducto,
                    'nombre': producto_obj.nombre,
                    'stock': str(producto_obj.stock),
                    'categoria': producto_obj.categoria,
                    'imagen': str(producto_obj.imagen),
                    'precio': str(producto_obj.precio),
                    'estado': producto_obj.estado,
                    'cantidad': cantidad
                }
                lista_productos.append(producto_dict)

                # Descuento del stock
                if producto_obj.stock >= cantidad:
                    producto_obj.stock -= cantidad
                    producto_obj.save()

            # Guardar en el modelo Carrito
            carrito = Carrito.crear_carrito(lista_productos)

            data = json.dumps(lista_productos)

            return JsonResponse(data, safe=False)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")

    return HttpResponseNotAllowed(['POST'])
# formato del json nuevo esto recibe{
#   "productos": [
#     {"id": 1, "cantidad": 10},
#     {"id": 2, "cantidad": 10},
#     {"id": 3, "cantidad": 10},
#     {"id": 4, "cantidad": 10}
#   ]
# }
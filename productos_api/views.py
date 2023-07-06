import json
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests as req
from .models import *   
from .serializers import * 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
class ProductoViews(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

def productos_api(req):
    productos = Producto.objects.all().values('id','nombre','precio')
    return JsonResponse({'productos':list(productos)})

    
def home_view(request):
    return render(request, 'home.html')

def hola_mundo(req):
    
    url = 'http://192.168.137.1:5000/api/v1/test/saludo'
    r = req.get(url)
    respuesta =r.json()
    print(respuesta['saldo'])
    return HttpResponse(respuesta)


def consulta(request):
    url = 'http://191.112.16.202:8000/api/producto/'
    r = req.get(url)
    respuesta = r.json()
    print(respuesta)
    return HttpResponse(respuesta)

def user(req):
    
    url = 'http://192.168.137.1:5000/api/v1/test/user'
    r = req.get(url)
    respuesta =r.json()
    print(respuesta)
    return HttpResponse(respuesta)

@api_view(['GET'])
@permission_classes([AllowAny])
def Carrito_api(req):
    Carritos = Carrito.objects.all().values('id','fecha','nombre','direccion','productos')
    return JsonResponse({'carritos':list(Carritos)})

@csrf_exempt
def agregar_a_lista(request):
    lista_productos = []

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            productos = data['productos']
            nombre = data['nombre']
            direccion = data['direccion']

            # Verificar si nombre y dirección están vacíos
            if not nombre or not direccion:
                return HttpResponseBadRequest("Nombre y dirección son campos requeridos.")

            for producto in productos:
                id_producto = producto['id']
                cantidad = producto['cantidad']

                producto_obj = get_object_or_404(Producto, pk=id_producto)
                producto_dict = {
                    'id': producto_obj.id,
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
                else:
                    # No hay suficiente stock
                    return HttpResponseBadRequest("No existe stock suficiente para el producto con ID: " + str(id_producto))

            # Guardar en el modelo Carrito
            carrito = Carrito.objects.create(nombre=nombre, direccion=direccion)

            for producto_dict in lista_productos:
                producto_id = producto_dict['id']
                cantidad = producto_dict['cantidad']
                carrito_producto = CarritoProducto.objects.create(
                    carrito=carrito,
                    producto=Producto.objects.get(id=producto_id),
                    cantidad=cantidad
                )

            data = json.dumps(lista_productos)

            return JsonResponse(data, safe=False)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")

    return HttpResponseNotAllowed(['POST'])

# formato del json nuevo esto recibe
# {
#   "productos": [
#     {
#       "id": "1",
#       "cantidad": 1
#     },
#     {
#       "id": "2",
#       "cantidad": 2
#     }
#   ],
#   "nombre": "juan",
#   "direccion": "su casa"
# }
@csrf_exempt
def enviar_productos(request):
    if request.method == 'POST':
        # Obtener los valores del formulario
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        foto = request.POST.get('foto')

        # Crear el diccionario con los valores del producto
        producto = {
            "Nombre": nombre,
            "Codigo": codigo,
            "Descripcion": descripcion,
            "Precio": precio,
            "Stock": stock,
            "Foto": foto
        }

        # Enviar el producto a la URL deseada
        url_destino = 'http://191.112.16.202:8000/api/producto/insert'
        response = req.post(url_destino, json=producto)

        if response.status_code == 200:
            # El producto se envió correctamente
            context = {
                'mensaje': 'Producto enviado correctamente',
                'producto': producto
            }
            return render(request, 'enviar_productos.html', context)
        else:
            # Hubo un error al enviar el producto
            context = {
                'error': 'Error al enviar el producto'
            }
            return render(request, 'enviar_productos.html', context)
    else:
        # Si es una solicitud GET, simplemente renderiza el formulario vacío
        return render(request, 'enviar_productos.html')

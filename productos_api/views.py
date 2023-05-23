from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
import requests as req
from .models import *   
from .serializers import * 

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
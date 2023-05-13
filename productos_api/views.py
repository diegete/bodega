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


from django.urls import include, path
from .views import *
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from productos_api import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViews,'productos')

#instalar requests 
urlpatterns = [
    path('', home_view, name='home'),
    path('api/',include(router.urls)),
    path('api/v1/productos',productos_api,name='productos' ),
    path('docs/', include_docs_urls(title='Api productos')),
    path('api/respuesta', hola_mundo, name='respuesta'),
    path('api/user',user,name='usuarios'),
    path('api/v1/productos/solicitud', views.agregar_a_lista, name='lista_productos'),

]
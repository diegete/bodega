from django.urls import include, path
from .views import *
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from productos_api import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViews,'productos')

urlpatterns = [
    path('', home_view, name='home'),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Api productos')),

]
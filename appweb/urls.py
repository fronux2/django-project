from unicodedata import name
from django.urls import path, include
from .views import MarcaViewset, home, contacto, galeria, agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset,\
MarcaViewset, politicas, error_facebook
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),    
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('politicas', politicas, name="politicas"),
    path('error_facebook', error_facebook, name="error_facebook"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls))

]
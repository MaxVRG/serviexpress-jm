from django.urls import path
from . import views
from .views import admin_login_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('reservahora/', views.reservahora, name='reservahora'),
    path('login/', views.login_view, name='login'),
    path('login/admin/', views.adminlogin, name='adminlogin'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('adminlogin/', admin_login_view, name='adminlogin'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),  
    path('registro-empleado/', views.registrar_empleado, name='registro_empleado'),
    path('registro-servicio/', views.registrar_servicio, name='registro_servicio'),
    path('proveedores/', views.registro_proveedor, name='registro_proveedor'),
    path('proveedor/<int:id>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('realizar_pedido/<int:proveedor_id>/', views.realizar_pedido, name='realizar_pedido'),
    path('verpedidos/', views.vista_pedidos, name='verpedidos'),
    path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

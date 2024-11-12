from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('reservahora/', views.reservahora, name='reservahora'),
    path('login/login/', views.login, name='login'),
    path('login/adminlogin/', views.adminlogin, name='adminlogin'),
    path('login/registrar/', views.registrar, name='registrar'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
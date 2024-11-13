from django.urls import path
from . import views
from .views import admin_login_view

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
]
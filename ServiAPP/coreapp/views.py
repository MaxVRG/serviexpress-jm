from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'coreapp/home.html')


def servicios(request):
    return render(request, 'coreapp/servicios.html')

def reservahora(request):
    return render(request, 'coreapp/reservahora.html')

def login(request):
    return render(request, 'coreapp/login/login.html')

def adminlogin(request):
    return render(request, 'coreapp/login/adminlogin.html')

def registrar(request):
    return render(request, 'coreapp/login/registrar.html')







def register(request):
    if request.method == 'POST':
        run = request.POST['run']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        username = request.POST['username']
        email = request.POST['email']
        telefono = request.POST['telefono']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Validar que las contraseñas coincidan
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'coreapp/register.html')
        
        # Validar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'coreapp/register.html')
        
        # Validar si el correo electrónico ya está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return render(request, 'coreapp/register.html')
        
        # Crear el usuario
        user = User.objects.create_user(
            username=username,
            first_name=nombre,
            last_name=apellidos,
            email=email,
            password=password
        )
        
        # Guardar otros datos adicionales si es necesario (ejemplo: run o teléfono)
        user.save()
        
        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        return redirect(reverse('login'))
    
    return render(request, 'coreapp/login/registrar.html')
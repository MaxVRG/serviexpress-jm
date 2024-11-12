from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import UsuarioRegistroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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



def registrar_usuario(request):
    if request.method == "POST":
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = form.cleaned_data["password"]  # Puedes agregar hashing aquí
            usuario.save()
            return redirect("login")  # Redirige al usuario al inicio de sesión
    else:
        form = UsuarioRegistroForm()
    
    return render(request, "coreapp/login/registrar.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')  # Mensaje de éxito
            return redirect('home')  # Redirige al inicio o a otra página

        else:
            messages.error(request, 'Credenciales incorrectas')  # Mensaje de error
            return render(request, 'coreapp/login/login.html')
    
    return render(request, 'coreapp/login/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')
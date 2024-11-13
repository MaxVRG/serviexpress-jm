from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def home(request):
    return render(request, 'coreapp/home.html')

def servicios(request):
    return render(request, 'coreapp/servicios.html')

def reservahora(request):
    return render(request, 'coreapp/reservahora.html')

def adminlogin(request):
    return render(request, 'coreapp/login/adminlogin.html')

def adminpanel(request):
    return render(request, 'coreapp/adminpanel.html')
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso!')
            return redirect('home')
        else:
            messages.error(request, 'Error en el registro. Por favor, verifica los datos.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'coreapp/login/registrar.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso!')
            return redirect('home')
        else:
            messages.error(request, 'Email o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'coreapp/login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def admin_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:  
                login(request, user)
                messages.success(request, 'Bienvenido al panel de administración.')
                return redirect('/adminpanel/')  
            else:
                messages.error(request, 'Acceso denegado. Solo los administradores pueden ingresar.')
                return redirect('adminlogin')
        else:
            messages.error(request, 'Email o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'coreapp/login/adminlogin.html', {'form': form})
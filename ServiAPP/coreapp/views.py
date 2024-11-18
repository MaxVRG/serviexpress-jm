from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .forms import EmpleadoForm
from .forms import ServicioForm
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm
from django.shortcuts import get_object_or_404

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



def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('adminpanel')  
    else:
        form = EmpleadoForm()
    
    return render(request, 'coreapp/panel/registro-empleado.html', {'form': form})


def registrar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('adminpanel')  
    else:
        form = ServicioForm()
    
    return render(request, 'coreapp/panel/registro-servicio.html', {'form': form})



def registro_proveedor(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        producto_form = ProductoForm(request.POST, request.FILES)
        if proveedor_form.is_valid() and producto_form.is_valid():
            proveedor = proveedor_form.save()
            producto = producto_form.save(commit=False)
            producto.proveedor = proveedor
            producto.save()
            return redirect('adminpanel') 
    else:
        proveedor_form = ProveedorForm()
        producto_form = ProductoForm()

    proveedores = Proveedor.objects.prefetch_related('productos').all()
    return render(request, 'coreapp/panel/registro-proveedor.html', {
        'proveedor_form': proveedor_form,
        'producto_form': producto_form,
        'proveedores': proveedores,
    })

def eliminar_proveedor(request, id):
    if request.method == "POST":
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.delete()
        return redirect('registro_proveedor')  # Redirige a la lista después de eliminar
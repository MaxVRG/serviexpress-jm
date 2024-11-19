from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, BoletaForm, CustomAuthenticationForm, EmpleadoForm, ServicioForm, ProveedorForm, ProductoForm, ReservaForm
from .models import Proveedor, Producto, Pedido
from .models import Reserva, Boleta
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.utils import timezone
from datetime import timedelta

def vista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'coreapp/panel/verpedidos.html', {'pedidos': pedidos})

def home(request):
    return render(request, 'coreapp/home.html')

def servicios(request):
    return render(request, 'coreapp/servicios.html')

def reservahora(request):
    return render(request, 'coreapp/reservahora.html')

def adminlogin(request):
    return render(request, 'coreapp/login/adminlogin.html')

def informes(request):
    return render(request, 'coreapp/panel/informes.html')

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
            return redirect('registro_proveedor') 
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
        return redirect('registro_proveedor')
    

def realizar_pedido(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    productos = proveedor.productos.all()

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        producto = get_object_or_404(Producto, id=producto_id)

        Pedido.objects.create(
            proveedor=proveedor,
            producto=producto,
            cantidad=cantidad,
            fecha_pedido=now()
        )
        return redirect('registro_proveedor')  

    return render(request, 'coreapp/panel/pedidos.html', {'proveedor': proveedor, 'productos': productos})




def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id_pedido=pedido_id)
    pedido.delete()
    return redirect('verpedidos') 


def reservahora(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva realizada con éxito.')
            return redirect('reservahora')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ReservaForm()
    
    return render(request, 'coreapp/reservahora.html', {'form': form})



def generar_boleta(request):
    boleta = None  
    
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        if form.is_valid():
            boleta = form.save()  

            return render(request, 'coreapp/panel/boleta.html', {'boleta': boleta, 'form': form})
    else:
        form = BoletaForm()


    return render(request, 'coreapp/panel/boleta.html', {'form': form, 'boleta': boleta})


def generar_pedido(request):
    pedidos = Pedido.objects.all()  
    total = sum(pedido.producto.precio * pedido.cantidad for pedido in pedidos)  

    return render(request, 'coreapp/panel/generar_pedidos.html', {'pedidos': pedidos, 'total': total})



def informes(request):

    ahora = timezone.now()
    inicio_mes = ahora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)  
    fin_mes = ahora.replace(day=28, hour=23, minute=59, second=59, microsecond=999999)  

 
    pedidos_mes = Pedido.objects.filter(fecha_pedido__gte=inicio_mes, fecha_pedido__lte=fin_mes).count()

    
    reservas_mes = Reserva.objects.filter(fecha_reserva__gte=inicio_mes, fecha_reserva__lte=fin_mes).count()


    visitas_mes = 240
    visitas_mensuales = [120, 150, 180, 130, 170, 160, 190, 200, 210, 220, 240, 250]

    return render(request, 'coreapp/panel/informes.html', {
        'visitas_mes': visitas_mes,
        'pedidos_mes': pedidos_mes,
        'reservas_mes': reservas_mes,  
        'visitas_mensuales': visitas_mensuales,
    })

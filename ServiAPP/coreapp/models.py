from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.timezone import now

class CustomUser(AbstractUser):
    run = models.CharField(
        max_length=12, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{7,8}-[\dkK]$',
                message='RUN debe tener formato 12345678-9'
            )
        ]
    )
    telefono = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Número de teléfono debe estar en formato: +999999999'
            )
        ]
    )
    
    email = models.EmailField(unique=True)
    

    nombre_completo = models.CharField(max_length=200)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'run', 'nombre_completo', 'telefono']

    def __str__(self):
        return self.email
    


class Empleado(models.Model):
    run = models.CharField(max_length=12, unique=True, help_text='RUN del empleado')
    
    nombres = models.CharField(max_length=100, help_text='Nombres del empleado')
    apellidos = models.CharField(max_length=100, help_text='Apellidos del empleado')
    
    email = models.EmailField(unique=True, help_text='Correo electrónico del empleado')
    telefono = models.CharField(max_length=15, blank=True, help_text='Teléfono del empleado')
    
    cargo = models.CharField(max_length=100, help_text='Cargo del empleado')
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class Servicio(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=200, help_text='')
    descripcion = models.TextField(help_text='')
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'   


class Proveedor(models.Model):
    empresa = models.CharField(max_length=100)
    correo = models.EmailField()
    rubro = models.CharField(max_length=100)

    def __str__(self):
        return self.empresa

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.proveedor.empresa}'
    


class Pedido(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, related_name='pedidos')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='pedidos')
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateTimeField(default=now)
    id_pedido = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.proveedor.empresa}"
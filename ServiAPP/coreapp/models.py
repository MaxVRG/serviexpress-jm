from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

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
    nombre = models.CharField(max_length=200, help_text='Nombre del servicio')
    descripcion = models.TextField(help_text='Descripción del servicio')
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='Precio del servicio')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'   
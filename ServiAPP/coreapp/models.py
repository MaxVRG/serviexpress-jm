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
    
    # Hacer que email sea obligatorio y único
    email = models.EmailField(unique=True)
    
    # Campo para nombre completo
    nombre_completo = models.CharField(max_length=200)
    
    # Definir qué campo se usará para el login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'run', 'nombre_completo', 'telefono']

    def __str__(self):
        return self.email
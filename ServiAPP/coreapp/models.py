from django.db import models

class Usuarios(models.Model):
    run = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Puedes usar hashing luego para seguridad

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.nombre_usuario}"

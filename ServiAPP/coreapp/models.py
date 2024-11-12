from django.db import models
from django.contrib.auth.hashers import make_password
from django.db import models

class Usuarios(models.Model):
    run = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.nombre} {self.apellidos}"

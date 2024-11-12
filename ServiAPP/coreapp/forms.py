from django import forms
from .models import Usuarios

class UsuarioRegistroForm(forms.ModelForm):
    confirmar_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = Usuarios
        fields = ['run', 'nombre', 'apellidos', 'nombre_usuario', 'email', 'telefono', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            self.add_error("confirmar_password", "Las contraseñas no coinciden.")
        
        return cleaned_data

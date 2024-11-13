from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Tu contraseña debe contener al menos 8 caracteres.'
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Ingresa la misma contraseña para verificación.'
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('run', 'email', 'nombre_completo', 'telefono', 'username', 'password1', 'password2')
        labels = {
            'run': 'RUN',
            'email': 'Correo electrónico',
            'nombre_completo': 'Nombre completo',
            'telefono': 'Teléfono',
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': None, 
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
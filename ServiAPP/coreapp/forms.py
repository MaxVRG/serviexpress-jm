from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Empleado
from .models import Servicio,Proveedor,Producto,Reserva, Boleta


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


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['run', 'nombres', 'apellidos', 'email', 'telefono', 'cargo']
        labels = {
            'run': 'RUN',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'cargo': 'Cargo',
        }
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio']
        labels = {
            'nombre': 'Nombre del Servicio',
            'descripcion': 'Descripción del Servicio',
            'precio': 'Precio del Servicio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'correo', 'rubro']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['imagen', 'nombre', 'cantidad', 'precio']


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['run', 'marca', 'modelo', 'fecha_reserva', 'hora_reserva']
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'type': 'date'}),
            'hora_reserva': forms.TimeInput(attrs={'type': 'time'}),
        }


class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['rut', 'direccion', 'fecha', 'descripcion_servicios', 'total']
        widgets = {
            'fecha': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'descripcion_servicios': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
        }
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut: 
            raise forms.ValidationError("El RUT es obligatorio.")
        return rut
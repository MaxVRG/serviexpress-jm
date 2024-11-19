from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Empleado,Servicio,Producto,Proveedor,Pedido,Reserva,Boleta

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'run', 'nombre_completo', 'telefono', 'is_staff')
    search_fields = ('email', 'username', 'run', 'nombre_completo')
    ordering = ('email',)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'run', 'nombre_completo', 'telefono', 'password1', 'password2'),
        }),
    )
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('username', 'run', 'nombre_completo', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Pedido)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('run', 'nombres', 'apellidos', 'email', 'telefono', 'cargo') 
    search_fields = ('run', 'nombres', 'apellidos', 'email')  
    list_filter = ('cargo',)  
    ordering = ('nombres',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)
    list_filter = ('precio',)



@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'correo', 'rubro')
    search_fields = ('empresa', 'rubro')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'proveedor')
    search_fields = ('nombre', 'proveedor__empresa')


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('run', 'marca', 'modelo', 'fecha_reserva', 'hora_reserva')
    list_filter = ('fecha_reserva', 'marca')
    search_fields = ('run', 'modelo', 'marca')


@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ('rut', 'direccion', 'fecha', 'total', 'impresa')  
    search_fields = ('rut', 'direccion')  
    ordering = ('-fecha',)  
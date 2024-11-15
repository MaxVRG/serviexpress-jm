from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Empleado

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


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('run', 'nombres', 'apellidos', 'email', 'telefono', 'cargo') 
    search_fields = ('run', 'nombres', 'apellidos', 'email')  
    list_filter = ('cargo',)  
    ordering = ('nombres',)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'run', 'nombre_completo', 'telefono', 'is_staff')
    search_fields = ('email', 'username', 'run', 'nombre_completo')
    ordering = ('email',)
    
    # Agregar estos campos para que funcione correctamente el admin
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

# Registrar el modelo y su clase admin
admin.site.register(CustomUser, CustomUserAdmin)
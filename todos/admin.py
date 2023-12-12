from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Todo
from .forms import CustomUserCreationForm

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'number', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'number', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'number')
    ordering = ('email',)
    filter_horizontal = ()

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Todo)

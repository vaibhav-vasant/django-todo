from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Todo, CustomUser

admin.site.register(Todo)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add any customizations here
    pass

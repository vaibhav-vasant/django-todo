from django.contrib import admin
from .models import Todo, CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'number', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Todo)
admin.site.register(CustomUser, CustomUserAdmin)

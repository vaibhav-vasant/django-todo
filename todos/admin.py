from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'deadline')
    list_filter = ('completed', 'deadline')
    search_fields = ('title', 'description')

admin.site.register(Todo, TodoAdmin)

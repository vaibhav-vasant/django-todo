from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'created', 'due_date')
    list_filter = ('completed', 'created', 'due_date')
    search_fields = ('title', 'description')

admin.site.register(Todo, TodoAdmin)

from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'deadline')

admin.site.register(Todo, TodoAdmin)

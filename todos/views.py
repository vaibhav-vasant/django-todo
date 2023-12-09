from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_datetime


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')


def add(request):
    title = request.POST['title']
    deadline_str = request.POST.get('deadline', None)
    deadline = parse_datetime(deadline_str) if deadline_str else None
    Todo.objects.create(title=title, deadline=deadline)

    return redirect('todos:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    deadline_str = request.POST.get('deadline', None)
    deadline = parse_datetime(deadline_str) if deadline_str else None

    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted
    todo.deadline = deadline

    todo.save()
    return redirect('todos:index')

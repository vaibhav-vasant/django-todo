from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for todo in context['todo_list']:
            todo.deadline = todo.deadline.strftime('%Y-%m-%d %H:%M:%S') if todo.deadline else 'No deadline'
        return context


def add(request):
    title = request.POST['title']
    deadline = request.POST.get('deadline')
    if deadline:
        deadline = timezone.make_aware(datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S'))
    else:
        deadline = None
    Todo.objects.create(title=title, deadline=deadline)

    return redirect('todos:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')

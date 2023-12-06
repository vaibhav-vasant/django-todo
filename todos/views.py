from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.exceptions import ValidationError

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')


def add(request):
    title = request.POST['title']
    deadline_str = request.POST.get('deadline', '')
    deadline = timezone.make_aware(timezone.datetime.strptime(deadline_str, '%m %d %Y'))

    if deadline < timezone.now():
        raise ValidationError('Deadline cannot be in the past.')

    Todo.objects.create(title=title, deadline=deadline)

    return redirect('todos:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    deadline_str = request.POST.get('deadline', '')
    deadline = timezone.make_aware(timezone.datetime.strptime(deadline_str, '%m %d %Y'))

    if isCompleted == 'on':
        isCompleted = True

    if deadline < timezone.now():
        raise ValidationError('Deadline cannot be in the past.')

    todo.isCompleted = isCompleted
    todo.deadline = deadline
    todo.save()
    return redirect('todos:index')

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos for the logged-in user."""
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')


@login_required

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title, user=request.user)

    return redirect('todos:index')


@login_required

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    todo.delete()

    return redirect('todos:index')


@login_required

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    else:
        isCompleted = False
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'todos/register.html'
    success_url = '/todos/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

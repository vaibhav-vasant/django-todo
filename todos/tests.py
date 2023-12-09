from django.test import TestCase
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


class TodoModelTest(TestCase):
    def test_deadline_field(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        todo = Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Retrieve the Todo item to verify its deadline
        saved_todo = Todo.objects.get(id=todo.id)
        self.assertEqual(saved_todo.deadline, deadline)


class TodoViewsTest(TestCase):
    def test_deadline_in_context(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Make a GET request to the view that lists Todo items
        response = self.client.get('/todos/')

        # Check if the deadline is in the context
        self.assertIn('deadline', response.context)


class TodoFormTest(TestCase):
    def test_form_deadline_field(self):
        # Create a form with deadline data
        deadline = timezone.now() + timezone.timedelta(days=7)
        form_data = {'title': 'Test Todo', 'description': 'Test Description', 'deadline': deadline}
        form = TodoForm(data=form_data)

        # Check if the form is valid and the deadline is cleaned correctly
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['deadline'], deadline)

from django.test import TestCase
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


class TodoModelTest(TestCase):

    def test_deadline_field(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=1)
        todo = Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Retrieve the Todo item
        saved_todo = Todo.objects.get(id=todo.id)

        # Check if the deadline is saved correctly
        self.assertEqual(saved_todo.deadline, deadline)


class TodoFormTest(TestCase):

    def test_deadline_field_in_form(self):
        # Create a TodoForm with data
        deadline = timezone.now() + timezone.timedelta(days=1)
        form_data = {'title': 'Test Todo', 'description': 'Test Description', 'deadline': deadline}
        form = TodoForm(data=form_data)

        # Check if the form is valid and deadline is handled correctly
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['deadline'], deadline)


class TodoViewTest(TestCase):

    def test_deadline_in_context(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=1)
        Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Make a request to the view that lists Todo items
        response = self.client.get('/todos/')

        # Check if the deadline is included in the context
        self.assertIn('deadline', response.context['todos'][0])
        self.assertEqual(response.context['todos'][0]['deadline'], deadline)

    # Here you would include other tests for your views, updating them to account for the 'deadline' field

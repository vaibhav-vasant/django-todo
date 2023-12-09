from django.test import TestCase
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


class TodoModelTest(TestCase):
    def test_deadline_field(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        todo = Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Retrieve the Todo item from the database to ensure it was saved correctly
        saved_todo = Todo.objects.get(id=todo.id)
        self.assertEqual(saved_todo.deadline, deadline)


class TodoViewTest(TestCase):
    def test_view_deadline_context(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Make a GET request to the view that lists Todo items
        response = self.client.get('/todos/')

        # Check if the deadline is included in the context
        self.assertIn('deadline', response.context[-1])


class TodoFormTest(TestCase):
    def test_form_deadline_field(self):
        # Create a form with deadline data
        form_data = {'title': 'Test Todo', 'description': 'Test Description', 'deadline': timezone.now() + timezone.timedelta(days=7)}
        form = TodoForm(data=form_data)

        # Check if the form is valid and the deadline field is handled correctly
        self.assertTrue(form.is_valid())
        self.assertIn('deadline', form.cleaned_data)

from django.test import TestCase
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


class TodoModelTest(TestCase):
    def test_todo_deadline_field(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        todo = Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Retrieve the Todo item
        retrieved_todo = Todo.objects.get(id=todo.id)

        # Check if the deadline matches
        self.assertEqual(retrieved_todo.deadline, deadline)


class TodoFormTest(TestCase):
    def test_todo_form_deadline_validation(self):
        # Create a form with a past deadline
        deadline = timezone.now() - timezone.timedelta(days=1)
        form_data = {'title': 'Test Todo', 'description': 'Test Description', 'deadline': deadline}
        form = TodoForm(data=form_data)

        # Check if the form is invalid as the deadline has passed
        self.assertFalse(form.is_valid())


class TodoViewTest(TestCase):
    def test_todo_view_deadline_context(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Make a request to the view that lists Todo items
        response = self.client.get('/todos/')

        # Check if the deadline is included in the context
        self.assertIn('deadline', response.context['todos'][0])


class TodoTemplateTest(TestCase):
    def test_todo_template_deadline_rendering(self):
        # Create a Todo item with a deadline
        deadline = timezone.now() + timezone.timedelta(days=7)
        Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)

        # Make a request to the view that lists Todo items
        response = self.client.get('/todos/')

        # Check if the deadline is rendered in the template
        self.assertContains(response, deadline.strftime('%Y-%m-%d'))

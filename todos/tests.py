from django.test import TestCase
from django.utils import timezone
from .models import Todo


class TodoModelTests(TestCase):

    def test_creating_todo(self):
        """Test the creation of a new todo item."""
        deadline = timezone.now() + timezone.timedelta(days=1)
        todo = Todo.objects.create(title='Test Todo', description='Test Description', deadline=deadline)
        self.assertIs(todo.title, 'Test Todo')
        self.assertIs(todo.description, 'Test Description')
        self.assertEqual(todo.deadline, deadline)

    def test_editing_todo(self):
        """Test editing an existing todo item."""
        todo = Todo.objects.create(title='Old Title', description='Old Description')
        todo.title = 'New Title'
        todo.description = 'New Description'
        todo.save()
        updated_todo = Todo.objects.get(id=todo.id)
        self.assertIs(updated_todo.title, 'New Title')
        self.assertIs(updated_todo.description, 'New Description')

    def test_todo_deadline_display(self):
        """Test the display of the deadline for a todo item."""
        deadline = timezone.now() + timezone.timedelta(days=1)
        todo = Todo.objects.create(title='Test Todo', deadline=deadline)
        self.assertEqual(todo.deadline, deadline)

    def test_todo_deadline_validation(self):
        """Test the deadline validation for a todo item."""
        deadline = timezone.now() - timezone.timedelta(days=1)
        with self.assertRaises(ValueError):
            Todo.objects.create(title='Test Todo', deadline=deadline)


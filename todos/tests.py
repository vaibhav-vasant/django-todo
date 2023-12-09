from django.test import TestCase
from django.utils import timezone
from .models import Todo


class TodoModelTest(TestCase):

    def setUp(self):
        self.deadline = timezone.now() + timezone.timedelta(days=1)
        Todo.objects.create(title='Test Todo', description='Test Description', deadline=self.deadline)

    def test_todo_creation(self):
        todo = Todo.objects.get(title='Test Todo')
        self.assertTrue(isinstance(todo, Todo))
        self.assertEqual(todo.__str__(), todo.title)
        self.assertEqual(todo.deadline, self.deadline)

    def test_todo_deadline(self):
        todo = Todo.objects.get(title='Test Todo')
        self.assertEqual(todo.deadline, self.deadline)
        self.assertTrue(todo.deadline > timezone.now())

    def test_todo_deadline_past(self):
        past_deadline = timezone.now() - timezone.timedelta(days=1)
        todo = Todo.objects.create(title='Past Todo', description='Past Description', deadline=past_deadline)
        self.assertTrue(todo.deadline < timezone.now())

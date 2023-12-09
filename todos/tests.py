from django.test import TestCase
from django.utils import timezone
from .models import Todo
from datetime import timedelta


class TodoModelTests(TestCase):

    def test_todo_deadline_future(self):
        """
        test_todo_deadline_future should return True for todos whose deadline is in the future
        """
        time_in_future = timezone.now() + timedelta(days=1)
        future_todo = Todo(deadline=time_in_future)
        self.assertIs(future_todo.is_deadline_in_future(), True)

    def test_todo_deadline_past(self):
        """
        test_todo_deadline_past should return False for todos whose deadline has passed
        """
        time_in_past = timezone.now() - timedelta(days=1)
        past_todo = Todo(deadline=time_in_past)
        self.assertIs(past_todo.is_deadline_in_future(), False)

    def test_todo_ordering_by_deadline(self):
        """
        Todos should be ordered by their deadline with the closest deadline first
        """
        time_now = timezone.now()
        Todo.objects.create(title='Todo 1', deadline=time_now + timedelta(days=2))
        Todo.objects.create(title='Todo 2', deadline=time_now + timedelta(days=1))
        Todo.objects.create(title='Todo 3', deadline=time_now + timedelta(days=3))

        todos = Todo.objects.all().order_by('deadline')
        self.assertEqual(todos[0].title, 'Todo 2')
        self.assertEqual(todos[1].title, 'Todo 1')
        self.assertEqual(todos[2].title, 'Todo 3')

    def test_todo_deadline_validation(self):
        """
        Creating a todo with a deadline in the past should raise a ValidationError
        """
        time_in_past = timezone.now() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            Todo.objects.create(title='Invalid Todo', deadline=time_in_past)

from django.test import TestCase
from django.utils import timezone
from .models import Todo
from .forms import TodoForm
from django.urls import reverse


class TodoModelTests(TestCase):

    def test_deadline_in_the_past(self):
        """
        Tests if the deadline of a Todo that is in the past is correctly identified.
        """
        time_in_the_past = timezone.now() - timezone.timedelta(days=1)
        past_todo = Todo(deadline=time_in_the_past)
        self.assertIs(past_todo.is_past_due(), True)

    def test_deadline_in_the_future(self):
        """
        Tests if the deadline of a Todo that is in the future is correctly identified.
        """
        time_in_the_future = timezone.now() + timezone.timedelta(days=1)
        future_todo = Todo(deadline=time_in_the_future)
        self.assertIs(future_todo.is_past_due(), False)


class TodoFormTests(TestCase):

    def test_form_with_future_deadline(self):
        """
        Tests if the form correctly handles a future deadline.
        """
        time_in_the_future = timezone.now() + timezone.timedelta(days=1)
        form_data = {'text': 'Test Todo', 'deadline': time_in_the_future}
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_past_deadline(self):
        """
        Tests if the form rejects a past deadline.
        """
        time_in_the_past = timezone.now() - timezone.timedelta(days=1)
        form_data = {'text': 'Test Todo', 'deadline': time_in_the_past}
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())


class TodoViewTests(TestCase):

    def test_deadline_displayed_in_template(self):
        """
        Tests if the deadline is correctly displayed in the template.
        """
        time_in_the_future = timezone.now() + timezone.timedelta(days=1)
        todo = Todo.objects.create(text='Test Todo', deadline=time_in_the_future)
        response = self.client.get(reverse('todos:todo_detail', args=(todo.id,)))
        self.assertContains(response, todo.deadline.strftime('%Y-%m-%d %H:%M:%S'))

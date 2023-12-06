from django.test import TestCase
from django.contrib.auth.models import User


class TodoTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_registration(self):
        response = self.client.post('/register/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_todo_list_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)

    def test_todo_list_unauthenticated(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 302)

    def test_todo_detail_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/todos/1/')
        self.assertEqual(response.status_code, 200)

    def test_todo_detail_unauthenticated(self):
        response = self.client.get('/todos/1/')
        self.assertEqual(response.status_code, 302)

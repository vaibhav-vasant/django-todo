from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass123'

    def test_registration(self):
        response = self.client.post(reverse('registration'), {
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_registration_with_mismatched_passwords(self):
        response = self.client.post(reverse('registration'), {
            'username': self.username,
            'password1': self.password,
            'password2': 'mismatch'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username=self.username).exists())

    def test_registration_with_existing_user(self):
        User.objects.create_user(username=self.username, password=self.password)
        response = self.client.post(reverse('registration'), {
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(username=self.username).count(), 1)

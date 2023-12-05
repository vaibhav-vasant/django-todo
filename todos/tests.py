from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationTestCase(TestCase):
    def test_registration_form(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_registration_form_validation(self):
        response = self.client.post(reverse('registration'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        self.assertEqual(users[0].username, 'testuser')

    def test_registration_form_validation_fail(self):
        response = self.client.post(reverse('registration'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')

    def test_successful_registration_redirect(self):
        response = self.client.post(reverse('registration'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123'
        }, follow=True)
        self.assertRedirects(response, reverse('registration_success'))

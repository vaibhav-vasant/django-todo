from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationTestCase(TestCase):
    def test_user_registration_form_display(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_user_registration_success(self):
        user_data = {
            'username': 'newuser',
            'password1': 'complexpassword',
            'password2': 'complexpassword'
        }
        response = self.client.post(reverse('signup'), user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('home'))

    def test_user_registration_password_length_validation(self):
        user_data = {
            'username': 'newuser',
            'password1': 'short',
            'password2': 'short'
        }
        response = self.client.post(reverse('signup'), user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2',
                             'This password is too short. It must contain at least 8 characters.')

# Replace 'signup' and 'home' with the actual names of the views used for signing up and redirecting after successful registration.
# Replace 'registration/signup.html' with the actual template used for the signup form.

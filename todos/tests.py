from django.test import TestCase


class UserRegistrationTestCase(TestCase):

    def test_registration_form_display(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_registration_form_validation(self):
        response = self.client.post('/register/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertRedirects(response, '/login/')

    def test_successful_registration_redirect(self):
        response = self.client.post('/register/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertRedirects(response, '/login/')

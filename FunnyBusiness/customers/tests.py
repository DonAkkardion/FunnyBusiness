from django.test import RequestFactory, TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.messages import get_messages
from unittest.mock import patch

from customers.views import registration_success

User = get_user_model()

class TestLoginUserView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login_url = reverse('LogIn')

    def test_login_user_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('Hub'))
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)

    def test_login_user_failure(self):
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertRedirects(response, reverse('LogIn'))
        self.assertNotIn('_auth_user_id', self.client.session)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Not possible to log in")

    def test_login_user_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')

@patch('Services.blockChainService.create_new_user')
class RegistrationSuccessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.client.login(username='jacob', password='top_secret')

    def test_registration_success_already_accessed(self, mock_create_new_user):
        session = self.client.session
        session['registration_success'] = True
        session.save()
        response = self.client.get(reverse('registration_successful'))
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'access_denied.html')

    def test_registration_success_first_access(self, mock_create_new_user):
        mock_create_new_user.return_value = {'private': 'mock_private_key'}
        response = self.client.get(reverse('registration_successful'))
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/registration_successful.html')
        session = self.client.session
        self.assertEqual(session.get('registration_success'), True)
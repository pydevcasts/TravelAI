

# Create your tests here.
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import json
User = get_user_model()
from rest_framework.test import APIClient


class LoginTests(APITestCase):
    def setUp(self):
        # ایجاد یک کاربر جدید برای تست
        self.username = 'admin'
        self.email = "admin@gmail.com"
        self.password = 'admin'
        self.user = User.objects.create_user(username=self.username,email=self.email, password=self.password)

    def test_login(self):
        url = reverse('rest_login') 
        data = {
            'email': self.email,
            'username': self.username,
            'password': self.password
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_login_invalid_credentials(self):
        url = reverse('rest_login')
        data = {
            'username': 'wronguser',
            'password': 'wrongpassword'
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LogoutTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def get_token(self):
        response = self.client.post(reverse('rest_login'), {'username': 'admin', 'email':'admin@gmail.com','password': 'admin'})
        print(response.content)
        self.assertEqual(response.status_code, 200, "Login failed: %s" % response.content)
        data = json.loads(response.content)
        if 'token' in data:
            self.token = data['token']
            print(self.token)
        
    def test_logout(self):
        headers = {'HTTP_AUTHORIZATION': f'Token {self.get_token}'}
        response = self.client.post(reverse('rest_logout'), **headers)

       # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Logged out successfully.')



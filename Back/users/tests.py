# Create your tests here.
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


class LoginTests(APITestCase):
    def setUp(self):
        # ایجاد یک کاربر جدید برای تست
        # self.username = 'admin'
        self.email = "admin@gmail.com"
        self.password = 'admin'
        self.user = User.objects.create_user(email=self.email, password=self.password)

    def test_login(self):
        url = reverse('rest_login')
        data = {
            'email': self.email,
            # 'username': self.username,
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
        response = self.client.post(reverse('rest_login'),
                                    {'username': 'admin', 'email': 'admin@gmail.com', 'password': 'admin'})
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


class RegisterTestCase(APITestCase):
    def setUp(self):
        # تنظیمات اولیه (اگر نیاز باشد)
        self.register_url = "/rest-auth/registration/"  # آدرس endpoint ثبت‌نام
        self.valid_data = {
            "email": "testuser@example.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        }
        self.invalid_data = {
            "email": "invalidemail",
            "password1": "short",
            "password2": "short",
        }

    def test_register_user_success(self):
        """تست ثبت‌نام موفق کاربر"""
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)  # بررسی وجود توکن دسترسی در پاسخ
        self.assertIn("refresh", response.data)  # بررسی وجود توکن تازه‌سازی
        self.assertTrue(User.objects.filter(email=self.valid_data["email"]).exists())

    def test_register_user_invalid_data(self):
        """تست ثبت‌نام با داده‌های نامعتبر"""
        response = self.client.post(self.register_url, self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertIn("password1", response.data)
        self.assertFalse(User.objects.filter(email=self.invalid_data["email"]).exists())

    def test_register_user_password_mismatch(self):

        mismatch_data = {
            "email": "testuser2@example.com",
            "password1": "Password123!",
            "password2": "DifferentPassword123!",
        }
        response = self.client.post(self.register_url, mismatch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", response.data)  # بررسی پیام خطا برای عدم تطابق رمز عبور
        self.assertFalse(User.objects.filter(email=mismatch_data["email"]).exists())


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from account.models import UserProfile
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserProfileRegistrationViewTest(TestCase):
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'national_id': '123456789',
            'password': 'testpassword',
        }

        self.client = APIClient()

    def test_user_registration(self):
        # Make a POST request to the user registration endpoint
        response = self.client.post('/api/account/register/', data=self.user_data)

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Add more assertions based on your API behavior
        # For example, check the response content, user existence in the database, etc.

    def test_duplicate_national_id(self):
        # Register a user before testing duplicate national id
        self.client.post('/api/account/register/', data=self.user_data)

        # Try to register another user with the same national id
        response = self.client.post('/api/account/register/', data=self.user_data)

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Add more assertions based on your API behavior
        # For example, check the response content for a specific error message

    def test_short_password(self):
        # Modify user data to have a short password
        self.user_data['password'] = '123'  # Assuming you want a minimum length of 4

        # Try to register a user with a short password
        response = self.client.post('/api/account/register/', data=self.user_data)

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Add more assertions based on your API behavior
        # For example, check the response content for a specific error message

    # Add more test methods as needed
    
    
    
    
# account/tests.py


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'national_id': '123456789',
            'password': 'password123',
        }

        # Create a user for testing
        get_user_model().objects.create_user(**self.user_data)

    def test_user_login(self):
        login_data = {
            'national_id': '123456789',
            'password': 'password123',
        }

        response = self.client.post(reverse('user-login'), data=login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Login successful')
        self.assertIn('access_token', response.data)
        self.assertIn('user', response.data)


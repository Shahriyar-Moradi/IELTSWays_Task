
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from exam.models import Exam  
from account.models import UserProfile   
from exam.serializers import ExamRegisterationSerializer  
from rest_framework.test import APITestCase


class ExamRegisterationViewTest(APITestCase):
    def setUp(self):
        # Create an exam for testing
        self.exam = Exam.objects.create(title='Test Exam')

    def test_exam_registration_without_authentication(self):
        # Data for the exam registration
        exam_registration_data = {'exam': self.exam.id}

        # Make the POST request without authentication
        response = self.client.post(reverse('exam_registeration'), data=exam_registration_data)

        # Assert the expected status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

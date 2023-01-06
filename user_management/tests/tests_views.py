from rest_framework.test import force_authenticate, APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from user_management.tests.base_user_management_test import BaseUserManagementTestCase
from user_management.views import UserTokenObtainPairView


class UserAccessTest(BaseUserManagementTestCase):

    def setUp(self):
        super().setUp()

    def test_get_access_token(self):
        """
        Test to ensure when the correct username/password is posted an access token is provided and 200 is returned.
        """
        client = APIClient()
        user = self.user
        url = reverse('token_obtain_pair')
        response = client.post(url, {"username": user.username, "password": self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        super().tearDown()

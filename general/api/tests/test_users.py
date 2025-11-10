from rest_framework.test import APITestCase
from rest_framework.views import status

from general.factories import UserFactory


class UserTestCase(APITestCase):
    def test_user_list(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)
        
        UserFactory.create_batch(20)
        
        url = "/api/users/"
        response = self.client.get(path=url, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertEqual(response.data["count"], 21)

from django.test import TestCase
from django.urls import reverse

class UsersSmokeTest(TestCase):
    def test_users_list_endpoint_exists(self):
        resp = self.client.get(reverse("users"))
        self.assertIn(resp.status_code, (200, 204, 301, 302))

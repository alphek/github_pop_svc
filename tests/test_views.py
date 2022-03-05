from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse


class TestDiscountCodeAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_github_popularity_true(self):
        url_params = {"username": "alphek", "repository_name": "github_pop_svc"}
        url = reverse("retrieve_github_popularity", kwargs=url_params)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert not response.json()["data"]["is_popular"]

    def test_retrieve_github_popularity_false(self):
        url_params = {"username": "freeCodeCamp", "repository_name": "freeCodeCamp"}
        url = reverse("retrieve_github_popularity", kwargs=url_params)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["data"]["is_popular"]

    # More tests should be added to test error cases

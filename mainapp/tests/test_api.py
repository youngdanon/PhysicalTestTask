from rest_framework.test import APITestCase


class WeekApiTestCase(APITestCase):
    def test_get(self):
        url = '/api/week/?date=06_01_2019'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'week': 2})

    def test_errors_catching(self):
        url = '/api/week/?date=06_13_2019'
        response = self.client.get(url)
        self.assertEqual(response.data, {'error': 'incorrect date'})

        url = '/api/week/'
        response = self.client.get(url)
        self.assertEqual(response.data, {'error': 'empty or not allowed query params'})

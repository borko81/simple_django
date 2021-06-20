from http import HTTPStatus
from django.test import TestCase


class AddBookFormTest(TestCase):
    def test_book_title_start_with_lowercase(self):
        response = self.client.post(
            "/create/", data={"title": 'a lower case'}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, 'Should start with upper case!', html=True
        )

    def test_description_stat_with_digit(self):
        response = self.client.post(
            "/create/", data={'description': 123}
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, 'Must not be start with digit!'
        )

from django.test import TestCase

from app.models import URL


class URLTestCase(TestCase):
    def setUp(self) -> None:
        """
        Set up the test case by creating a URL object with the original URL 'http://example.com'.

        This method is called before each test case is executed. It creates a
        new URL object in the database with the specified original URL.
        """
        URL.objects.create(original_url='http://example.com')

    def test_string_representation(self) -> None:
        url = URL.objects.first()
        assert str(url) == 'http://example.com'

    # def test_slug_generation(self) -> None:
    #     url = URL.objects.first()

    def test_redirect_to_original(self) -> None:
        url = URL.objects.first()
        assert url.original_url == 'http://example.com'

        response = self.client.get(f'/{url.slug}')

        redirect_status_code = 302
        assert response.status_code == redirect_status_code
        assert response['Location'] == 'http://example.com'

        assert URL.objects.count() == 1

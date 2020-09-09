from django.test import TestCase

# Create your tests here.


class TestViewsBag(TestCase):

    def test_get_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

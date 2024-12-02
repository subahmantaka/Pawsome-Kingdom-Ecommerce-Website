# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class CategoryViewTest(TestCase):
    def setUp(self):
        # Set up a test client and create a test product
        self.client = Client()
        self.product = Product.objects.create(
            title='Test Product',
            selling_price=100.0,
            discounted_price=80.0,
            description='Test Description',
            category='D',
            product_image='path/to/image.jpg'
        )

    def test_category_view_status_code(self):
        """
        Test that the category view returns a 200 status code.
        """
        response = self.client.get(reverse('category', args=['D']))
        self.assertEqual(response.status_code, 200)

    def test_category_view_functionality(self):
        """
        Test that the category view correctly filters products by category.
        """
        response = self.client.get(reverse('category', args=['D']))
        self.assertContains(response, self.product.title)

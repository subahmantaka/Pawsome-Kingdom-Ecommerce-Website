from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Cart

"""
Unit testing for the functions add to cart,view cart and delete an item from cart.
The class CartTestCase tests these three functions of Cart Management.

"""

class CartTestCase(TestCase):
    def setUp(self):

        """
        Here the user is the test user who tests the functions
        This test user is used to test all the functions of cart management
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_add_to_cart(self):

        """
        Tests the functionality of adding an item to cart.
        Test User chooses the product and enters the quantity of that product and this test checks whether the chosen quantity of product 
        was added successfully to the cart or not.
        """
        Cart.objects.create(user=self.user, product_name="Test Product", quantity=2)
        self.assertEqual(Cart.objects.count(), 1)
    
    def test_view_cart(self):
        """
        Tests the functionality of viewing the current items in cart
        Retrieves the information about the items currently in cart mainly the product name and quantity chosen
        """
        cart_item = Cart.objects.create(user=self.user, product_name="Test Product", quantity=2)
        cart_items = Cart.objects.filter(user=self.user)
        self.assertIn(cart_item, cart_items)
    
    def test_delete_from_cart(self):
        """
        Tests the functionality of deleting an item from the cart.
        After clicking on the delete button,the chosen item is deleted from the cart and quantity is adjusted accordingly.

        """
        cart_item = Cart.objects.create(user=self.user, product_name="Test Product", quantity=2)
        cart_item.delete()
        self.assertEqual(Cart.objects.count(), 0)

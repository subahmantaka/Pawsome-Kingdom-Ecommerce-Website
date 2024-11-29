from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    """
    Represents an item in the user's shopping cart.

    Attributes:
        user : The customer who uses this website.
        product_name : The name of the product.
        quantity: The quantity of the product added by the user in the cart.
        added_on (datetime): The date and time when the product was added to the cart.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    The customer who uses this website.
    :no-index:
    """
    
    product_name = models.CharField(max_length=255)
    """
    The name of the product.
    :no-index:
    """
    
    quantity = models.PositiveIntegerField(default=1)
    """
    The quantity of the product added to the cart by the user.
    :no-index:
    """
    
    added_on = models.DateTimeField(auto_now_add=True)
    """
    The date and time when the product was added to the cart.
    :no-index:
    """

    def __str__(self):
        """
        Returns the product name and quantity.

        Returns:
            str: a formatted string
        """
        return f"{self.product_name} (x{self.quantity})"


class Wishlist(models.Model):
    """
    -Allows User to add an item to wishlist 

    **Functionality**:
    -can add an item to wishlist
    -if user wants, can move the item to cart for purchase

    **Parameter**:
    -user: the customer who adds an item to wishlist
    -product_name: name of the item to be added
    -added_on: date and time at which item was added 
    """
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.product_name}"

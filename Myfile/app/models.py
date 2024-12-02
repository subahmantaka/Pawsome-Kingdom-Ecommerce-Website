"""
Models for the app.

This module contains the models for the app. It includes the Product model,
which represents the products in the application. The Product model has fields
for the title, selling price, discounted price, description, category, and 
product image. The category choices are predefined.
"""

from django.db import models

# Define category choices
CATEGORY_CHOICES=(
    ('D', 'Dog'),
    ('C', 'Cat'),
    ('B', 'Bird'),
    ('F', 'Fish'),
)
class Product(models.Model):
    """
    Product model representing the products in the application.

    Fields:
        title (CharField): The title of the product.
        selling_price (FloatField): The selling price of the product.
        discounted_price (FloatField): The discounted price of the product.
        description (TextField): A description of the product.
        category (CharField): The category of the product. Choices are Dog, Cat, Bird, Fish.
        product_image (ImageField): The image of the product, uploaded to the 'product' directory.
    """

    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to= 'product') 

    def str(self):
        """
        String representation of the Product model.

        Returns:
            str: The title of the product.
        """

        return self.title 

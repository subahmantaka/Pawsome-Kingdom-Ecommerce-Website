"""
Admin configuration for the app.

This module contains the registration of the Product model with the admin site
and the configuration for displaying the Product model in the admin interface.
"""
from django.contrib import admin
from . models import Product
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model.

    This class configures how the Product model is displayed in the admin interface.

    Attributes:
        list_display (list): The fields to display in the admin list view.
    """

    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'category', 'product_image']
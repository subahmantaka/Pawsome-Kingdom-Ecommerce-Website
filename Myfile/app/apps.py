"""
Application configuration for the app.

This module contains the application configuration class for the app.
"""

from django.apps import AppConfig

class AppConfig(AppConfig):
    """
    Configuration class for the app.

    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary key field.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

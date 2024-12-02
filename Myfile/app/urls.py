"""
URL configuration for the app.

This module contains the URL patterns for the app. It includes views for 
the home page, contact page, search functionality, category view, and 
product detail view. Static media files are also served through these URL patterns.
"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URL patterns
urlpatterns = [
    path("", views.home),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

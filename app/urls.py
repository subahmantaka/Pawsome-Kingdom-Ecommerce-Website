from django.urls import path
from . import views


"""
following are the urls using which we can visit the corresponding webpages of our website
calls from views
"""
urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'), 
    path('view_cart/', views.view_cart, name='view_cart'),
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
]

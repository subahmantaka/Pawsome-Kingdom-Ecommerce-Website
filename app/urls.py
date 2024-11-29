from django.urls import path
from . import views


"""
following are the urls using which we can visit the corresponding webpages of our website
calls from views
"""
urlpatterns = [

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'), #URL for accessing add to cart webpage
    path('view_cart/', views.view_cart, name='view_cart'), #URL for viweing cart webpage
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'), #URL for deleting an item from view wishlist webpage
    path('add_to_wishlist/',views.add_to_wishlist,name='add_to_wishlist'), #URL for adding an item to wishlist
    path('view_wishlist/',views.view_wishlist,name='view_wishlist'), #URL for vieweing thw wishlist webpage
    path('remove_from_wishlist<int:item_id>/',views.remove_from_wishlist,name='remove_from_wishlist'), #URL for removing an item from wishlist from view wishlist webpage 
    path('move_to_cart/<int:item_id>',views.move_to_cart,name='move_to_cart'), #URL for moving an item to cart from view wishlist webpage 
]
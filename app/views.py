from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cart

"""
Condition:
    - The `@login_required` decorator is applied to ensure that only logged-in users can access the cart functionalities.
    - If a user is not logged in, they will be redirected to the login page.
"""

@login_required
def add_to_cart(request):
    """
    Adds an item to the shopping cart.

    **Functionality**:
    - Handles POST requests to add an item to the cart.
    - If the request is a GET request, renders the `add_to_cart.html` template.

    **Returns**:
    - Redirects to the `view_cart` page upon successful addition.
    - Renders the `add_to_cart.html` template for GET requests.
    """
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity', 1))
        Cart.objects.create(user=request.user, product_name=product_name, quantity=quantity)
        return redirect('view_cart')
    return render(request, 'app/add_to_cart.html')

@login_required
def view_cart(request):
    """
    Displays items currently in the shopping cart.

    **Functionality**:
    - Retrieves all items added by the logged-in user to their cart.
    - Renders the `view_cart.html` template to display these items.

    **Returns**:
    - A rendered HTML page showing the user's cart items.
    """
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'app/view_cart.html', {'cart_items': cart_items})

@login_required
def delete_from_cart(request, item_id):
    """
    Deletes a specific item from the shopping cart.

    **Functionality**:
    - Identifies the item to delete using its `item_id` and the logged-in user.
    - Deletes the item from the database.
    - Redirects the user to the `view_cart` page after deletion.

    **Returns**:
    - A redirect to the `view_cart` page after the item is deleted.
    """
    cart_item = Cart.objects.get(id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

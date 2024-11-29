from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cart,Wishlist

"""
Condition:
    - The @login_required decorator is applied to ensure that only logged-in users can access the cart functionalities.
    - If a user is not logged in, they will be redirected to the login page.
"""

@login_required
def add_to_cart(request):
    """
    Adds an item to the shopping cart.

    **Functionality**:
    - Handles POST requests to add an item to the cart.
    - Renders the add_to_cart.html template with the product list.
    - Handles search functionality to find and add specific products.

    **Returns**:
    - Redirects to the view_cart page upon successful addition.
    - Renders the add_to_cart.html template for GET requests.
    """
    # Sample product data 
    products = [
        {"name": "Cat Food", "image_url": "/static/images/1.png"},
        {"name": "Dog Food", "image_url": "/static/images/2.png"},
        {"name": "Bird Seed", "image_url": "/static/images/3.png"},
    ]

    search_query = request.GET.get('search', '')
    if search_query:
        
        products = [product for product in products if search_query.lower() in product['name'].lower()]

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity', 1))
        Cart.objects.create(user=request.user, product_name=product_name, quantity=quantity)
        return redirect('view_cart')

    
    return render(request, 'app/add_to_cart.html', {'products': products, 'search_query': search_query})



@login_required
def view_cart(request):
    """
    Displays items currently in the shopping cart.

    **Functionality**:
    - Retrieves all items added by the logged-in user to their cart.
    - Renders the view_cart.html template to display these items.

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
    - Identifies the item to delete using its item_id and the logged-in user.
    - Deletes the item from the database.
    - Redirects the user to the view_cart page after deletion.

    **Returns**:
    - A redirect to the view_cart page after the item is deleted.
    """
    cart_item = Cart.objects.get(id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')




@login_required
def add_to_wishlist(request):
    """
    Adds an product to wishlist

    **Functionality**:
    -A list of already available products with picture and name is displayed on website from where the user
     can click on the wishlist button and add to the wishlist
    -User can also search for the name of a product and also add it to wishlist
    

    **Returns**:
    -redirects to view_wishlist webpage after an item was added to wishlist

    """
    products = [
        {"name": "Cat Food", "image_url": "/static/images/1.png"},
        {"name": "Dog Food", "image_url": "/static/images/2.png"},
        {"name": "Bird Seed", "image_url": "/static/images/3.png"},
    ]

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        Wishlist.objects.create(user=request.user, product_name=product_name)
        return redirect('view_wishlist')

    # Pass the list of products 
    return render(request, 'app/add_to_wishlist.html', {'products': products})





@login_required
def view_wishlist(request):
    """
    Currently Displays the items added in wishlist 

    **Functionality:**
    -User can move an item from wishlist to add it to cart 
    -User can view current items in wishlist

    **Returns**:
    -redirects to view_wishlist webpage after an item was added to wishlist
    """
    wishlist_items=Wishlist.objects.filter(user=request.user)
    return render(request,'app/view_wishlist.html',{'wishlist_items':wishlist_items})

@login_required
def remove_from_wishlist(request,item_id):
    """
    Removes an item from wishlist 

    **Functionality:**
    -If any item is no longer desired by the user,the user can remove it from their wishlist by clicking on the 
     remove button

     **Returns**:
    -redirects to view_wishlist webpage after an item was added to wishlist
    """
    wishlist_item=Wishlist.objects.get(id=item_id,user=request.user)
    wishlist_item.delete()
    return redirect('view_wishlist')

@login_required
def move_to_cart(request,item_id):
    """
    An item can be added to cart directly from the wishlist

    **Functionality:**
    -If User wishes to purchase any items currently added in their wishlist , they can do so by moving that item to 
     cart and the item will be added to the cart .After that the user can purchase the product using normal "add_to_cart" function

     **Returns**:
    -redirects to view_wishlist webpage after an item was added to wishlist
    """
    wishlist_item=Wishlist.objects.get(id=item_id,user=request.user)
    Cart.objects.create(user=request.user,product_name=wishlist_item.product_name,quantity=1)
    wishlist_item.delete()
    return redirect('view_wishlist')
from django.db.models import Count
from django.db.models import Q
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . models import Product

# Create your views here.
def home(request):
    """ 
    Renders the home page.
    
    :param request: The HTTP request object. 
    :return: The rendered home page. 
    """
    return render(request, "app/home.html")

def contact(request):
    """ 
    Renders the contact page.

    :param request: The HTTP request object. 
    :return: The rendered contact page.
    """
    return render(request, "app/contact.html")

def search(request):
    """
    Searches for products based on the query provided in the request.

    :param request: The HTTP request object.
    :return: The rendered search results page.
    """
    query = request.GET['search']
    product= Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html",locals())    
     

class CategoryView(View):
    """
    View to display products by category.

    :param request: The HTTP request object.
    :param val: The category value to filter products.
    :return: The rendered category page.
    """

    def get(self, request, val):
        product= Product.objects.filter(category=val)
        title= Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    """
    View to display product details.

    :param request: The HTTP request object.
    :param pk: The primary key of the product to display.
    :return: The rendered product detail page.
    """

    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())
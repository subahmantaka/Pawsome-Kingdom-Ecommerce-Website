from django.contrib import admin
from django.urls import path
from . import views
from your_app_name.views import home  # Replace 'your_app_name' with the name of your app

urlpatterns = [
   #path('admin/', admin.site.urls),
    path("",views.home),  # Add this line
]

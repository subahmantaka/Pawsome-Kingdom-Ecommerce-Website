from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


"""
The payment model is used to track the payment details
for the order. 
The foreign key here refers to the number associated with the 
the order. 
The amount refers to the total payment amount. 
The payment_date gives the timestamp for the payment. 
The payment status gives the status of the order, depending on whether the placement of the order was a success
or a failure. 
"""
# Payment model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])

    def __str__(self):
        return f"{self.user.username} - {self.payment_status} - {self.amount}"

"""
The order model represents an order placed by a user. 
The user refers to the user who placed the order in the system.
The order date gives us the timestamp for the creation of the order. 
The order details gives us details about the order items and details. 
The order details gives us the status of the order. 
For example: if the order has been delivered, the user will be "Delivered"
but if the order is yet to be delivered, the user see "Pending" written. 
"""

# Order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_details = models.TextField()
    order_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])

    def __str__(self):
        return f"{self.user.username} - {self.order_status}"

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Payment model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])

    def __str__(self):
        return f"{self.user.username} - {self.payment_status} - {self.amount}"

# Order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_details = models.TextField()
    order_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])

    def __str__(self):
        return f"{self.user.username} - {self.order_status}"

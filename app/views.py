from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment, Order

# Payment page view
@login_required
def payment_view(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        # Dummy payment processing
        payment = Payment.objects.create(user=request.user, amount=amount, payment_status="Success")
        return render(request, 'payment_success.html', {'payment': payment})
    return render(request, 'payment.html')

# Profile page view
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

# View orders page
@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'view_orders.html', {'orders': orders})


def home(request):
    return render(request, 'base.html')

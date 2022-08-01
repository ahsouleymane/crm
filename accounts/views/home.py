from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Customer, Order

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

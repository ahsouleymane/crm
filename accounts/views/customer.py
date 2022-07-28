from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Customer

# Create your views here.

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders,
    'order_count': order_count}

    return render(request, 'accounts/customer.html', context)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from accounts.models import Customer
from accounts.filters import OrderFilter
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    # permet de faire une filtre de recherche
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders,
    'order_count': order_count, 'myFilter': myFilter}

    return render(request, 'accounts/customer.html', context)

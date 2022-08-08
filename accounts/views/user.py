from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_users
from accounts.models import Customer

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):

    orders = request.user.customer.order_set.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}
    return render(request, 'accounts/user.html', context)
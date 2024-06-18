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
    LivrE = orders.filter(status='Livré').count()
    En_attente = orders.filter(status='En attente').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'LivrE':LivrE,
    'En_attente':En_attente}
    return render(request, 'accounts/user.html', context)
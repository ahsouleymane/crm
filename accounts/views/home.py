from django.shortcuts import render
from django.http import HttpResponse
from accounts.decorators import admin_only

from accounts.models import Customer, Order

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    LivrE = orders.filter(status='Livré').count()
    En_attente = orders.filter(status='En attente').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'LivrE':LivrE,
    'En_attente':En_attente}

    return render(request, 'accounts/dashboard.html', context)

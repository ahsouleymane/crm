from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

from accounts.models import Product

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

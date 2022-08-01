from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Product

# Create your views here.

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

from django.urls import path
from accounts.views import home, products, customer

urlpatterns = [
    path('', home.home),
    path('products/', products.products),
    path('customer/', customer.customer),
]
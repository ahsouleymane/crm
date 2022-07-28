from django.urls import path
from accounts.views import home, products, customer, createOrder, updateOrder, deleteOrder

urlpatterns = [
    path('', home.home, name="home"),
    path('products/', products.products, name="products"),
    path('customer/<str:pk_test>/', customer.customer, name="customer"),
    path('create_order/', createOrder.createOrder, name="create_order"),
    path('update_order/<str:pk>', updateOrder.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', deleteOrder.deleteOrder, name="delete_order"),
]

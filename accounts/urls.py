from django.urls import path
from accounts.views import home, products, customer, createOrder, updateOrder, deleteOrder, login, register, logout, user, account

urlpatterns = [

    path('user/', user.userPage, name="user_page"),
    
    path('account/', account.accountSettings, name="account"),

    path('login/', login.loginPage, name="login"),
    path('register/', register.registerPage, name="register"),
    path('logout/', logout.logoutUser, name="logout"),

    path('', home.home, name="home"),
    path('products/', products.products, name="products"),
    path('customer/<str:pk_test>/', customer.customer, name="customer"),

    path('create_order/<str:pk>/', createOrder.createOrder, name="create_order"),
    path('update_order/<str:pk>/', updateOrder.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', deleteOrder.deleteOrder, name="delete_order"),
]

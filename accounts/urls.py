from django.urls import path
from accounts.views import home, products, customer, createOrder, updateOrder, deleteOrder, login, register, logout, user, account
from django.contrib.auth import views as auth_views

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
    
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
         name="reset_password"),
    
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
         name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
         name="password_reset_confirm"),
    
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_done.html"), 
         name="password_reset_complete"),
]

from django.shortcuts import render
from accounts.forms import OrderForm

def createOrder(request):

    form = OrderForm
    if request.method == "POST":
        print('Printing post:', request.POST)

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
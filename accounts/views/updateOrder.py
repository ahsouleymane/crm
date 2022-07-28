from django.shortcuts import render, redirect
from accounts.forms import OrderForm
from accounts.models import Order

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        #print('Printing post:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
        return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
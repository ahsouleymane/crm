from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from accounts.forms import OrderForm
from accounts.models import Order
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/updateOrder_form.html', context)
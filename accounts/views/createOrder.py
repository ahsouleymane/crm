from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from accounts.forms import OrderForm
from accounts.models import Customer, Order
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):

    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        #print('Printing post:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()

        return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)
from django.shortcuts import render, redirect
from accounts.forms import OrderForm

def createOrder(request):

    form = OrderForm
    if request.method == "POST":
        #print('Printing post:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
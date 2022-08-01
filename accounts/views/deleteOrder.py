from django.shortcuts import redirect, render
from accounts.models import Order
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete_order.html', context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from accounts.forms import CustomerForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        
        if form.is_valid():
            form.save()
        
    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)
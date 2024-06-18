from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    context = {}
    return render(request, 'accounts/account_settings.html', context)
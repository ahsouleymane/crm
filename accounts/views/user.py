from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def userPage(request):

    context={}
    return render(request, 'accounts/user.html', context)
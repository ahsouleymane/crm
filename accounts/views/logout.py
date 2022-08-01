from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages

def logoutUser(request):

    logout(request)
    messages.info(request, 'User logout successfuly !!!')

    return redirect('login')
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username / password is incorrect !!!')

        context = {}
        return render(request, 'accounts/login.html', context)
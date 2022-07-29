from django.shortcuts import render
from accounts.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

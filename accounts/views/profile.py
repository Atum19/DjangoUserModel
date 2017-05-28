from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms import UserCreationForm, UserLoginForm

User = get_user_model()


def home(request):
    print(request.user.profile.city)
    return render(request, 'base.html', {})


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        # form.save()
        cln_username = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=cln_username)
        # User.objects.
        login(request, user_obj)
        return HttpResponseRedirect('/')

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

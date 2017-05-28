from django.shortcuts import render


def home(request):
    print(request.user.profile.city)
    return render(request, 'home.html', {})

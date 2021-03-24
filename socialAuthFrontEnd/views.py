from django.shortcuts import render

# Create your views here.


def googleLogin(request):
    return render(request, 'google.html', context={})

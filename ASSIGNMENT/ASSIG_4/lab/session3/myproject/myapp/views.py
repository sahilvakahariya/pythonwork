from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, "home.html")

def explore(request):
    return render(request, "explore.html")

def profile(request):
    return render(request, "profile.html")


from django.shortcuts import render


def login_view(request):
    return render(request, "frontend/login.html")


def home_view(request):
    return render(request, "frontend/home.html")

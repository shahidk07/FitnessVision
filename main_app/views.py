from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def exercises(request):
    return render(request, "exercises.html")
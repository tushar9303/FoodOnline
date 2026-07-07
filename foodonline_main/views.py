from django.shortcuts import render


def home(request):
    return render(request, "foodonline_main/home.html")
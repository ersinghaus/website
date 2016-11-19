from django.shortcuts import render

def home(request):
    return render(request, "hub/Home.html")

def about(request):
    return render(request, "hub/about.html")

def math(request):
    return render(request, "hub/Math.html")

def science(request):
    return render(request, "hub/Science.html")

def history(request):
    return render(request, "hub/History.html")

def art(request):
    return render(request, "hub/Arts.html")

def signup(request):
    return render(request, "hub/Sign up.html")

def register(request):
    return render(request, "hub/Register.html")



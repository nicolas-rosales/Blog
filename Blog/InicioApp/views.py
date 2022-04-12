from ast import Return
from django.shortcuts import render
from django.http import HttpRequest



# Vistas creadas para la App de Inicio #

def index(request):
    return render(request,"InicioApp/index.html")

def about(request):
    return render(request, "InicioApp/about.html")

def blog(request):
    return render(request, "InicioApp/blog.html")

def user(request):
    return render(request, "InicioApp/userpage.html")

def contact(request):
    return render(request, "InicioApp/contact.html")
from ast import Return
from django.shortcuts import render
from django.http import HttpRequest

def login(request):
    return render(request,"CuentasApp/login.html")
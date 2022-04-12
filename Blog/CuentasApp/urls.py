from django.urls import path
from InicioApp.views import *
from CuentasApp.views import *

urlpatterns = [
    path('CuentasApp/login/', login, name='login'),
      
]
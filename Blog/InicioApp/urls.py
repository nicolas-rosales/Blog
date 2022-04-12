from django.urls import path
from InicioApp.views import *

urlpatterns = [
    path('', index, name=''),
    path('InicioApp/index/', index,name="home"),
    path('InicioApp/about/', about,name="about"),
    path('InicioApp/blog/', blog,name="blog"),
    path('InicioApp/userpage/', user,name="userpage"),
    path('InicioApp/contact/', contact,name="contact"),
]

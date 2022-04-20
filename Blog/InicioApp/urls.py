from django import views
from django.views import *
from django.urls import path
from InicioApp.views import *


urlpatterns = [
    path('', index, name=''),
    path('InicioApp/index/', index,name="home"),
    path('InicioApp/about/', about,name="about"),
    path('InicioApp/pages/', readpost,name="pages"),
    path('InicioApp/userpage/', user,name="userpage"),
    path('InicioApp/contact/', contact,name="contact"),
    path('InicioApp/createpost', createpost,name="createpost"),
    
    
    # path('post/list', views.postlist.as_view(), name= "List"),
    # path(r'^(?p<pk>\d+)$', views.postdetalle.as_view(), name = "Detail"),
    
    
]

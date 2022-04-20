from ast import Return
from django.shortcuts import render
from django.http import HttpRequest
from django.forms import forms
from requests import post
from InicioApp.models import Post
from InicioApp.forms import CreatePost




# Vistas creadas para la App de Inicio #

def index(request):
    return render(request,"InicioApp/index.html")

def about(request):
    return render(request, "InicioApp/about.html")

# def pages(request):
#     return render(request, "InicioApp/pages.html")

def user(request):
    return render(request, "InicioApp/userpage.html")

def contact(request):
    return render(request, "InicioApp/contact.html")


# Vistas Creadas para Crear Post #

def createpost(request):
    if request.method == "POST":
        informacion = CreatePost(request.POST)
        print(informacion)
        
        if informacion.is_valid():
            data = informacion.cleaned_data
            post = Post(title=data['title'],
                        content=data['content'],
                        publish_date=data['publish_date'],
                        )
            post.save()
            return render(request, 'InicioApp/userpage.html')
    else:
        informacion = CreatePost()
    return render(request,"InicioApp/createpost.html", {"informacion":informacion})

# Vista para hacer lectura de la base de datos de los post #

def readpost(request):
    post = Post.objects.all()
    contexto = {"post": post}
    return render(request, "InicioApp/pages.html", contexto)



# Vista Basada en Clases #

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy


class postlist(ListView):
    model = Post
    template_name = "InicioApp/postlist.html"
    
class postdetelle(DetailView):
    model = Post
    template_name = "InicioApp/postdetail.html"
    
class postcreacion(CreateView):
    model = Post
    template_name = "InicioApp/postcreate.html"
    fields = ['title', 'subtitle', 'content', 'publish_date']

class postactualizacion(UpdateView):
    model = Post
    success_url = "InicioApp/post/list"    
    fields = ['title', 'subtitle', 'content', 'publish_date']

class postborrar(DeleteView):
    model = Post
    success_url = "InicioApp/post/list"








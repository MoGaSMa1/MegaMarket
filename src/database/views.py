from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.


def home_page(request):
    Author = models.Author.objects.get()
    Gener =  models.Gener.objects.get()
    return render(request, 
                  template_name="home_page.html", 
                  context={'Author' : Author,
                           'Gener' : Gener
                        }) 

def login(request):
    return render(request, 
                  template_name="login.html", 
                  context={}) 

def registration(request):
    return render(request, 
                  template_name="registration.html", 
                  context={}) 

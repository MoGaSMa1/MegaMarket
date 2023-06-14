from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from .forms import UserRegisterForm

# Create your views here.


def home_page(request):
    return render(request, 
                  template_name="home_page.html", 
                  context={
                        }) 

def create(request):
    if request.method == "POST":
        author = models.Author()
        author.Author = request.POST.get("author")
        author.save()
    return render(request, 
                  template_name="create.html", 
                  context={
                        }) 

def login(request):
    return render(request, 
                  template_name="login.html", 
                  context={}) 

def registration(request):
    print(request.POST.get("username"))

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}.')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
        return render(request, 
                    template_name="registration/registration.html", 
                    context={'form': form}) 

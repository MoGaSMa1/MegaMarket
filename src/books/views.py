from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.utils import timezone
from django.urls import reverse
from cart.forms import CartAddBookForm


def home_page(request):
    authors = models.Author.objects.all()
    serieses = models.Series.objects.all()
    geners = models.Gener.objects.all()
    publishs = models.Publish.objects.all()
    books = models.Book.objects.all()
    # search = models.Book.objects.filter(body__icontains='framework')
    # print(books)
    return render(request,
                  template_name='home_page.html',
                  context={'books': books,
                   'authors': authors,
                   }
                )

def book_detail(request, pk):
    book = get_object_or_404(models.Book, pk=pk)
    cart_book_form = CartAddBookForm()
    available = book.available
    if available == True:
        available = "In stock"
    else:
        available = "Out of stock"
    return render(request,
                  'book.html',
                  {'book': book,
                   'cart_book_form': cart_book_form,
                   'available': available})


def create_book(request):
    authors = models.Author.objects.all()
    serieses = models.Series.objects.all()
    geners = models.Gener.objects.all()
    publishs = models.Publish.objects.all()
    if request.method == "POST":
       
        name = request.POST.get("name")
        img = request.POST.get("img")
        price = request.POST.get("price")

        author_id = request.POST.get("author")
        author = models.Author.objects.get(pk=int(author_id))
        author = author

        series_id = request.POST.get("series")
        series = models.Series.objects.get(pk=int(series_id))
        series = series

        gener_id = request.POST.get("gener")
        gener = models.Gener.objects.get(pk=int(gener_id))
        gener = gener

        year = request.POST.get("year")
        pages =  request.POST.get("pages")
        binding = request.POST.get("binding")
        formatt = request.POST.get("formatt")
        isbn = request.POST.get("isbn")
        weight = request.POST.get("weight")
        ager =request.POST.get("ager")

        publish_id = request.POST.get("publish")
        publish = models.Publish.objects.get(pk=int(publish_id))
        publish = publish

        quantity = request.POST.get("quantity")
        available = request.POST.get("availability")
        rating = request.POST.get("rating")
        created = timezone.now()
        modified = timezone.now()

        models.Book.objects.create( name=name, 
                                    img=img, 
                                    price=price,
                                    author=author, 
                                    series=series,
                                    gener=gener, 
                                    year=year, 
                                    pages=pages, 
                                    binding=binding, 
                                    formatt=formatt, 
                                    isbn=isbn, 
                                    weight=weight, 
                                    ager=ager, 
                                    publish=publish, 
                                    quantity=quantity, 
                                    available=available,
                                    rating=rating,
                                    created=created,
                                    modified=modified)
    return render(request, 
                  template_name="create_book.html", 
                  context={"authors": authors,
                           "serieses": serieses,
                           "geners": geners,
                           "publishs":  publishs
                        }) 

def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        models.Author.objects.create(Author=name)
    return render(request, 
                  template_name="create_author.html", 
                  context={
                        }) 

def create_series(request):
    if request.method == "POST":
        name = request.POST.get("name")
        models.Series.objects.create(Series=name)
    return render(request, 
                  template_name="create_series.html", 
                  context={
                        }) 


def create_gener(request):
    if request.method == "POST":
        name = request.POST.get("name")
        models.Gener.objects.create(Gener=name)
    return render(request, 
                  template_name="create_gener.html", 
                  context={
                        }) 

def create_publish(request):
    if request.method == "POST":
        name = request.POST.get("name")
        models.Publish.objects.create(Publish=name)
    return render(request, 
                  template_name="create_publish.html", 
                  context={
                        }) 


def create(request):

    return render(request,
                  template_name='create.html',
                  context={}
                )










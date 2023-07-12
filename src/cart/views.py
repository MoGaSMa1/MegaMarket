from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from books.models import Book
from .cart import Cart
from .forms import CartAddBookForm


# Create your views here.


def cart(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})

@require_POST
def cart_add(request, pk):
    print('1')
    cart = Cart(request)
    book = get_object_or_404(Book, pk=pk)
    print(book)
    print(type(book))
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart')

def cart_remove(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, pk=pk)
    cart.remove(book)
    return redirect('cart')
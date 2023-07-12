from decimal import Decimal
from django.conf import settings
from books.models import Book


class Cart(object):

    def __init__(self, request):

        #  Инициализация корзины

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, Book, quantity=1, update_quantity=False):

        #  Добавить продукт в корзину или обновить его количество

        book_pk = str(Book.pk)
        if book_pk not in self.cart:
            self.cart[book_pk] = {'quantity': 0,
                                    'price': str(Book.price)}
        if update_quantity:
            self.cart[book_pk]['quantity'] = quantity
        else:
            self.cart[book_pk]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True
    
    def remove(self, Book):

        # Удаление товара из корзины

        book_pk = str(Book.pk)
        if book_pk in self.cart:
            del self.cart[book_pk]
            self.save()

    def __iter__(self):

        # Перебор элементов в корзине и получение продуктов из базы данных.

        book_pks = self.cart.keys()
        
        # получение объектов book и добавление их в корзину
        books = Book.objects.filter(id__in=book_pks)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):

        #Подсчет стоимости товаров в корзине

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        
        # Удаление корзины из сессии

        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
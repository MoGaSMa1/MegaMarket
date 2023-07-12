from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('book_create/', views.create_book, name='book_create'),
    path('author_create/', views.create_author, name='author_create'),
    path('gener_create/', views.create_gener, name='gener_create'),
    path('publish_create/', views.create_publish, name='publish_create'),
    path('series_create/', views.create_series, name='series_create'),
    path('', views.home_page, name='home_page'),
    path('book_detail/<int:pk>', views.book_detail, name='book_detail'),
]
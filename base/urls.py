from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.genres, name='genres'),
    path('authors/', views.authors, name='authors'),
    path('books/', views.books, name='books'),
    path('genre/details/<str:slug>/', views.genre_details, name='genre_details'),
    path('author/details/<str:slug>/', views.author_details, name='author_details'),
    path('book/details/<str:slug>/', views.book_details, name='book_details'),
    path('register/book/<str:slug>/', views.register_book, name='register_book'),
]

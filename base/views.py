from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from base.models import GenreModel, AuthorModel, BookModel


def gba(request):
    genres = GenreModel.objects.all()
    authors = AuthorModel.objects.all()
    books = BookModel.objects.all()
    context = {
        'genres': genres,
        'authors': authors,
        'books': books,
    }
    return context


def home(request):
    context = gba(request)
    return render(request, 'home.html', context)


def genres(request):
    context = gba(request)
    return render(request, 'base/genres.html', context)


def authors(request):
    context = gba(request)
    return render(request, 'base/authors.html', context)


def books(request):
    context = gba(request)
    return render(request, 'base/books.html', context)


def genre_details(request, slug):
    genre = get_object_or_404(GenreModel, slug=slug)
    genres = GenreModel.objects.all().exclude(slug=slug)
    authors = AuthorModel.objects.all()
    books = BookModel.objects.all()
    context = {
        'genre': genre,
        'genres': genres,
        'authors': authors,
        'books': books,
    }
    return render(request, 'base/genre_details.html', context)


def author_details(request, slug):
    author = get_object_or_404(AuthorModel, slug=slug)
    authors = AuthorModel.objects.all().exclude(slug=slug)
    genres = GenreModel.objects.all()
    books = BookModel.objects.all()
    context = {
        'author': author,
        'authors': authors,
        'genres': genres,
        'books': books,
    }
    return render(request, 'base/author_datails.html', context)


def book_details(request, slug):
    book = get_object_or_404(BookModel, slug=slug)
    books = BookModel.objects.all().exclude(slug=slug)
    genres = GenreModel.objects.all()
    authors = AuthorModel.objects.all()
    context = {
        'book': book,
        'books': books,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'base/book_details.html', context)


def register_book(request, slug):
    if request.user.is_authenticated:
        book = get_object_or_404(BookModel, slug=slug)
        if book not in [rb.book for rb in request.user.registeredbookmodel_set.all()]:
            request.user.registeredbookmodel_set.create(book=book)
            messages.success(request, f'{book} was added to the book.')
        else:
            messages.error(request, f'{book} This book has already been added')
        return HttpResponseRedirect(reverse('account:my_books', kwargs={'slug': slug}))
    else:
        return HttpResponseRedirect(reverse('login'))

import json
import requests

from django.shortcuts import render
from django.views.generic import View

from .keys import google_books_api


class FindBookView(View):
    def get(self, request):
        return render(request, 'library/find_book.html')

    def post(self, request):
        if 'isbn_search' in request.POST:
            isbn = request.POST.get('isbn')
            books = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={google_books_api}')

            books = books.json()

            books_to_display = []

            for book in books['items']:
                book = book['volumeInfo']
                book_title = book.get('title', '')
                book_subtitle = book.get('subtitle', '')
                book_authors = book.get('authors', '')
                book_published_date = book.get('publishedDate', '')
                book_language = book.get('language', '')

                book_image = book.get('imageLinks', '')
                if book_image:
                    book_image = book_image.get('thumbnail')

                books_to_display.append({'title': book_title,
                                         'subtitle': book_subtitle,
                                         'authors': book_authors,
                                         'published_date': book_published_date,
                                         'language': book_language,
                                         'image': book_image
                                         })
            ctx = {
                'books': books_to_display
            }

        return render(request, 'library/find_book.html', ctx)


class ShelvesView(View):
    def get(self, request):
        ...

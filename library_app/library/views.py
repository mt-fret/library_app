import json

from django.shortcuts import render
from django.views.generic import View
import requests
from .keys import google_books_api
class AddBookView(View):
    def get(self, request):
        return render(request, 'library/find_book.html')

    def post(self, request):
        isbn = request.POST.get('isbn')
        books = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={google_books_api}')
        books = books.json()
        ctx = {
            'books': books
        }
        return render(request, 'library/find_book.html', ctx)


class ShelvesView(View):
    def get(self, request):
        ...

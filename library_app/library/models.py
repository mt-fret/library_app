from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=512)


class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField()
    language = models.CharField(max_length=10)
    publisher = models.ManyToManyField(Publisher)
    image = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=13)


class Shelve(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

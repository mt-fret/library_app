from django.db import models


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

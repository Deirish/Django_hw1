from django.db import models

# models from Book Catalog

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# models from Book Library

class UserReader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Library(models.Model):
    book_title = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    author = models.ManyToManyField(Author)
    readers = models.ManyToManyField(UserReader)
    books_availability = models.BooleanField(default=True)

    def __str__(self):
        return self.book_title





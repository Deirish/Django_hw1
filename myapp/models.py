from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

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
    books_availability = models.BooleanField()

    def __str__(self):
        return self.book_title

# models from blog-site


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nickname


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_of_writing = models.DateTimeField()


class Comment(Article):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTE = (
        (DISLIKE, 'Dislike:('),
        (LIKE, 'Like:)')
    )
    votes = models.SmallIntegerField(choices=VOTE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')










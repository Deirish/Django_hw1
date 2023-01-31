from django.contrib import admin
from .models import Author, Book, UserReader, Library

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UserReader)
admin.site.register(Library)

# Register your models here.

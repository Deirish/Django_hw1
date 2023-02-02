from django.contrib import admin
from .models import Author, Book, UserReader, Library, User, Article, Comment, LikeDislike

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UserReader)
admin.site.register(Library)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeDislike)

# Register your models here.

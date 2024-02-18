from django.contrib import admin
from Libros.models import Book

# Register your models here.
admin.site.register(Book, list_display=['book_pk', 'title', 'author', 'price'])
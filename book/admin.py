from django.contrib import admin
from book.models import *

# Register your models here.
class BookAdmin (admin.ModelAdmin):
    list_display = ['title', 'author', 'date_published', 'number_of_pages', 'type_of_book']
    list_filter = ()
    search_fields = ['title', 'author', 'date_published', 'number_of_pages', 'type_of_book']
    list_per_page = 25

admin.site.register(Book, BookAdmin)
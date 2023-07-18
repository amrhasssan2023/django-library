from django.contrib import admin
from .models import Book, Category

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        'photo_book',
        'photo_author',
        'pages',
        'price',
        'rental_price',
        'rental_periud',
        'total_rental',
        'status',
        'active',
        'category',
    ]
    search_fields = ['title']
    list_filter = ['title','author']


admin.site.register(Book,BookAdmin)
admin.site.register(Category)


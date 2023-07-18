from rest_framework import serializers
from .models import Book, Category


class BookSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
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

class CategorySerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'name',
        ]
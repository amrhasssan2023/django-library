from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
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
        'category',
        ]

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control'}),
            'photo_book' : forms.FileInput(attrs={'class' : 'form-control'}),
            'photo_author' : forms.FileInput(attrs={'class' : 'form-control'}),
            'pages' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'rental_price' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'rental_periud' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'total_rental' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(attrs={'class' : 'form-control'}),

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm, CategoryForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()


    context = {
        'books' : Book.objects.all(),
        'category' : Category.objects.all(),
        'form' : BookForm(),
        'formcat' : CategoryForm(),
        'allbook' : Book.objects.filter(active=True).count()

    }
    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)
    context = {
        'books' : search,
        'category' : Category.objects.all(),

    }

    return render(request, 'pages/books.html',context)

def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'add_book' : book_save,
    }

    return render(request, 'pages/update.html',context)

def delete(request, id):
    delete_book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        delete_book.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')
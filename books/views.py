from django.shortcuts import render
from .models import Book
from .filter import BookFilter

# Create your views here.



def home_page(request):
    books = Book.objects.all().order_by('rating_book__rating')[:6]

    context={'books' : books}
    return render(request, 'home.html', context)


def all_books(request):
    books = BookFilter(request.GET,queryset=Book.objects.all())

    context = {'books' : books}   
    return render(request, 'all_books.html', context) 
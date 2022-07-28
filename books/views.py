from django.shortcuts import render
from .models import Book, Comment
from .filter import BookFilter
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.



def home_page(request):
    books = Book.objects.all().order_by('rating_book__rating')[:6]

    context={'books' : books}
    return render(request, 'home.html', context)


def all_books(request):
    books = BookFilter(request.GET,queryset=Book.objects.all())

    context = {'books' : books}   
    return render(request, 'all_books.html', context) 


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    comments = Comment.objects.all().filter(post_book__exact=book)

    context = {'book' : book, 'comments' : comments}
    return render(request, 'book_detail.html', context)
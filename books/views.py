from django.shortcuts import render
from .models import Book

# Create your views here.



def home_page(request):
    books = Book.objects.all().order_by('rating_book__rating')[:6]

    context={'books' : books}
    return render(request, 'home.html', context)
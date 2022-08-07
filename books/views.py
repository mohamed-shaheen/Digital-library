from django.shortcuts import render
from .models import Book, Comment, Rating
from .filter import BookFilter
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count

# Create your views here.



def home_page(request):
    books = Book.objects.all().order_by('-rating_book__rating')[:6]


    context={'books' : books}
    return render(request, 'home.html', context)


def all_books(request):
    books = BookFilter(request.GET,queryset=Book.objects.all())

    context = {'books' : books}   
    return render(request, 'all_books.html', context) 


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
 
    if request.user.is_authenticated:    
        if request.method == 'POST':
            try:
                num = int(request.POST.getlist('star')[0])
                Rating.objects.create(
                    user=request.user,
                    book=book,
                    rating=num
                )
            except:
                pass    
    #comments = Comment.objects.all().filter(post_book__exact=book)
    rating_mod = book.rating_book
    rating = rating_mod.aggregate(Avg('rating'))
    people = {
        'exl':rating_mod.filter(rating=5).count(),
        'good':rating_mod.filter(rating=4).count(),
        'avr':rating_mod.filter(rating=3).count(),
        'poor':rating_mod.filter(rating=2).count(),
        'bru':rating_mod.filter(rating=1).count(),
        'total':rating_mod.all().count(),
        }

    context = {'book' : book, 'rating' : rating, 'people':people}
    return render(request, 'book_detail.html', context)
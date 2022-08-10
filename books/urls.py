from django.urls import path, include
from . import views




app_name = 'books'





urlpatterns = [
    path('', views.home_page, name='home'),
    path('books/', views.all_books, name = 'all_books'),
    path('books/<str:slug>/', views.book_detail, name='book_detail'),
    path('book/share/', views.book_add, name = 'book_add'),
]
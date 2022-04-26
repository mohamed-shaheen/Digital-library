from django.urls import path, include
from . import views




app_name = 'books'





urlpatterns = [
    path('', views.home_page, name='home'),
    path('books/', views.all_books, name = 'all_books'),
]
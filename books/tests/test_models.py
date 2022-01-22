from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from books.models import Book, Category, Rating
from django.db.models import Sum, Avg







class BookModelTest(TestCase):

    fixtures = ['user.json', 'book.json', 'category.json', 'rating.json']


    @classmethod
    def setUpTestData(cls):
        pass

    def test_averge(self):
        book = Book.objects.all()
        rate = book.filter(title='Dalil book').aggregate(Avg('rating_book__rating'))
        self.assertEqual(rate['rating_book__rating__avg'], 7)    

from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from books.models import Book, Category, Rating







class ShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='mohamed', email='example@email.com',  password='testpass')
        user2 = User.objects.create_user(username='ahmed', email='example@email.com',  password='testpass2')
        user3 = User.objects.create_user(username='mostafa', email='example@email.com',  password='testpass3')
        book=Book.objects.create(title='some title', author='author name', publish_dt="1/1/2019", category = "", uploaded_by=user)
        book2=Book.objects.create(title='some title2', author='author name2', publish_dt="1/1/2019", category = "", uploaded_by=user2)
        book3=Book.objects.create(title='some title3', author='author name3', publish_dt="1/1/2019", category = "", uploaded_by=user3)
        book4=Book.objects.create(title='some title4', author='author name4', publish_dt="1/1/2019", category = "", uploaded_by=user3)
        rating = Rating.objects.create()

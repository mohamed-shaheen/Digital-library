from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from books.models import Book, Category, Rating
from django.core.files import File as DjangoFile







#class BookModelTest(TestCase):
#
#    @classmethod
#    def setUpTestData(cls):
#        #user = User.objects.create_user(username='mohamed', email='example@email.com',  password='testpass')
#        #user2 = User.objects.create_user(username='ahmed', email='example@email.com',  password='testpass2')
#        #user3 = User.objects.create_user(username='mostafa', email='example@email.com',  password='testpass3')
#        #category = Category.objects.create(title="action", created_by=user)
#        #category2 = Category.objects.create(title="drama", created_by=user)
#        #category3 = Category.objects.create(title="fantasy", created_by=user)
#        #book=Book.objects.create(title='some title', author='author name', publish_dt="1/1/2019", uploaded_by=user, file=DjangoFile(open("D:\projects\Digital_library\src"), "C-30 If.pdf"))
#        #book2=Book.objects.create(title='some title2', author='author name2', publish_dt="1/1/2019", uploaded_by=user2, file=DjangoFile(open("D:\projects\Digital_library\src"), "C-30 If.pdf"))
#        #book3=Book.objects.create(title='some title3', author='author name3', publish_dt="1/1/2019", uploaded_by=user3, file=DjangoFile(open("D:\projects\Digital_library\src"), "C-30 If.pdf"))
#        #book4=Book.objects.create(title='some title4', author='author name4', publish_dt="1/1/2019", uploaded_by=user3, file=DjangoFile(open("D:\projects\Digital_library\src"), "C-30 If.pdf"))
#        #rating = Rating.objects.create(user=user2, book=book, rating="5")
#        #rating2 = Rating.objects.create(user=user2, book=book2, rating="9")
#        #rating3 = Rating.objects.create(user=user3, book=book, rating="7")
#        #rating4 = Rating.objects.create(user=user3, book=book2, rating="3")
#
#    def test_averge(self):
#        book_av = Rating.objects.get(book__title="some title")
#        self.assertEqual(book_av.rating_avg(), '6')    

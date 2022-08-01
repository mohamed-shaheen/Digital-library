from books.views import book_detail
from django_unicorn.components import UnicornView
from books.models import Comment, Book
from django.shortcuts import get_object_or_404



class CommentBookView(UnicornView):
    

    comment = ""
    bookid: int = 0

 
    def comments_v(self):
        if self.bookid:
            return []    
        print(self.bookid) 
        comments = Comment.objects.all().filter(post_book_id__exact=int(self.bookid))
        return comments
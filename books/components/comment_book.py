from django_unicorn.components import UnicornView
from books.models import Comment, Book




class CommentBookView(UnicornView):
    

    comment_post = ""
    bookid: int = 0
    comments: Comment = None
    book: Book = None
    
    def mount(self):
        self.comments = Comment.objects.all()
        return super().mount()

        
    def comments_v(self, num=0):
        if num > 0:
           self.bookid=num
        self.book = Book.objects.get(id=self.bookid)
        Comment.objects.create(
            post_by=self.request.user,
            post_book=self.book,
            post=self.comment_post
        )
        print(self.bookid)
        self.comment_post= ""
        self.comments = Comment.objects.filter(post_book_id__exact=self.book.id)



    def book_v(self):
        return self.comments    
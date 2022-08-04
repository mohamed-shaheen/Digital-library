from django_unicorn.components import UnicornView
from books.models import Comment, Book




class CommentBookView(UnicornView):
    

    comment_post = ""
    bookid: int = 0
    comments: Comment = None
    book: Book = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.bookid = kwargs.get("bookid") 
        self.comments = Comment.objects.filter(post_book_id__exact=self.bookid).order_by('-post_at')


        
    def comments_submit(self):

        if self.comment_post:
            self.book = Book.objects.get(id=self.bookid)
            Comment.objects.create(
                post_by=self.request.user,
                post_book=self.book,
                post=self.comment_post
            ) 
            self.comment_post= ""
            self.comments = Comment.objects.filter(post_book_id__exact=self.book.id).order_by('-post_at')
        else:
            pass    



    def comments_context(self): 
        return self.comments    
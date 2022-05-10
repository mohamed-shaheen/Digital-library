from django_unicorn.components import UnicornView, QuerySetType
from books.models import Book


class SearchBarView(UnicornView):
    
    search = ""
    #books: QuerySetType[Book] = Book.objects.none()
 
    def books_s(self):
        if not self.search:
            return []
        books = Book.objects.filter(title__icontains=self.search)
        return books

    #class Meta:
    #    exclude = ("books",)

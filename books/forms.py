from django import forms
from .models import Book




class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["title", "isbn", "author", "publisher", "publish_dt", "description", "category", "cover_img", "file"]



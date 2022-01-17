from atexit import register
import site
from django.contrib import admin
from .models import Book, Category, Rating
# Register your models here.



admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Rating)
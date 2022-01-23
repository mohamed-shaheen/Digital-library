from atexit import register
import site
from django.contrib import admin
from .models import Book, Category, Rating, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Comment)
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'post'


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Rating)
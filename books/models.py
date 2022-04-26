from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db.models import CheckConstraint, Q, UniqueConstraint
from .validators import FileValidator
# Create your models here.


validate_file_book = FileValidator(max_size=1024 * 1024 * 60,  content_types=('application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'book/user_{0}/{1}/{2}'.format(instance.uploaded_by, instance.title, filename)

class Book(models.Model):

    title = models.CharField(max_length=100, help_text=_("The book title"), verbose_name=_("Title"))
    added_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Added at"))
    isbn = models.CharField(max_length=13, help_text=_("International Standard Book Number"), validators=[RegexValidator(regex=r'\d{13}|\d{10}', message=_("10 or 13 digits"))], blank=True, null=True, verbose_name=_("IBSN"))
    author = models.CharField(max_length=50, verbose_name=_("Author"))
    publisher = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Publisher"))
    publish_dt = models.DateField(verbose_name=_("Published at"))
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("Description"))
    category = models.ManyToManyField("Category", blank=True, related_name="book_cat", verbose_name=_("Category"))
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_user", verbose_name=_("Uploaded by"))
    cover_img = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name=_("Cover image"))
    file = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(['pdf', 'docx'], message=_("the file must be '.pdf' or '.docx'.")), validate_file_book], help_text=_("Book type : pdf or doc"), verbose_name=_("Book file"))
    slug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"), allow_unicode=True)


    def save(self, *args, **kwargs):
        if not self.slug :
           self.slug = slugify(self.title, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books") 

    #def get_absolute_url(self):
    #    return reverse("", kwargs={"id" : self.id, "slug": self.slug})

    def __str__(self):
        return self.title[:15]



class Category(models.Model):

    title = models.CharField(max_length=60, verbose_name=_("Title"))
    description = models.TextField(max_length=400, blank=True, null=True, verbose_name=_("Description"))
    img = models.ImageField(upload_to="Category_img/", width_field="200", height_field="200", blank=True, null=True, verbose_name=_("Image"))
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Created by"))
    slug = models.SlugField(blank=True, null=True, allow_unicode=True, verbose_name=_("Slug"))


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title[:10]

    #def get_absolute_url(self):
    #    return reverse('\', kwargs={'pk': self.pk}) 



class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_user", verbose_name=_("User"))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rating_book", verbose_name=_("Book"))
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], verbose_name=_("Rating") )
    rating_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Rating at"))


    def __str__(self):
        return str(self.rating)

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
        constraints = [
            CheckConstraint(check=Q(rating__range=(0, 10)), name='valid_rate'),
            UniqueConstraint(fields=['user', 'book'], name='rating_once')
        ]

    #def get_absolute_url(self):
    #    return reverse('\', kwargs={'pk': self.pk})  



class Comment(models.Model):

    post_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user", verbose_name=_("User"))
    post_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comment_book", verbose_name=_("Book"))
    post = models.TextField(max_length=1000, verbose_name=_("Comment"))
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Replies"))
    post_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Posted at"))


    def __str__(self):
        return '{0}comment by {1} on {2}'.format(self.pk,self.post_by.username, self.post_book.title)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")



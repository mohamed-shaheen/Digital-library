from re import T
from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, FileExtensionValidator
# Create your models here.



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'book/user_{0}/{1}'.format(instance.uploaded_by, filename)

class Book(models.Model):

    title = models.CharField(max_length=100, help_text=_("The book title"), verbose_name=_("Title"))
    added_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Added at"))
    isbn = models.CharField(max_length=13, help_text=_("International Standard Book Number"), validators=[RegexValidator(regex=r'\d{13}|\d{10}', message=_("10 or 13 digits"))], blank=True, null=True, verbose_name=_("IBSN"))
    author = models.CharField(max_length=50, verbose_name=_("Author"))
    publisher = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Publisher"))
    publish_dt = models.DateField(verbose_name=_("Published at"))
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("Description"))
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Uploaded by"))
    cover_img = models.ImageField(upload_to="cover_img/", blank=True, null=True, verbose_name=_("Cover image"))
    file = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(['pdf'], message=_("the file must be '.pdf'."))], verbose_name=_("Book file"))
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


from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
# Create your models here.




class Book(models.Model):

    title = models.CharField(max_length=100, help_text=_("The book title"), verbose_name=_("Title"))
    added_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Added at"))

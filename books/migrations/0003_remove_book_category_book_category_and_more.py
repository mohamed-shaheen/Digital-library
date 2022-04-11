# Generated by Django 4.0.1 on 2022-01-20 21:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_cover_img_alter_book_isbn_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='book_cat', to='books.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Rating'),
        ),
    ]
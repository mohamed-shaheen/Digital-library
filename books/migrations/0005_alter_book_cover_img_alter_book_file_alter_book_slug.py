# Generated by Django 4.0.1 on 2022-05-11 08:40

import books.models
import books.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_category_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.user_directory_path, verbose_name='Cover image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(help_text='Book type : pdf or doc', upload_to=books.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx'], message="the file must be '.pdf' or '.docx'."), books.validators.FileValidator(content_types=('application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'), max_size=62914560)], verbose_name='Book file'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
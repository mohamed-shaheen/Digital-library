# Generated by Django 4.0.1 on 2022-01-23 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_remove_book_category_book_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='book_cat', to='books.Category', verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(max_length=1000, verbose_name='Comment')),
                ('post_at', models.DateTimeField(auto_now_add=True, verbose_name='Posted at')),
                ('post_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_book', to='books.book', verbose_name='Book')),
                ('post_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.comment', verbose_name='Replies')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]

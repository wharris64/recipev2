# Generated by Django 2.2.6 on 2020-01-12 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0002_author_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='favorites',
        ),
    ]

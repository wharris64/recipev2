# Generated by Django 2.2.6 on 2020-01-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(related_name='fave', to='recipebox.Recipe'),
        ),
    ]

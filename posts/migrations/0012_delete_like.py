# Generated by Django 3.2.3 on 2021-06-01 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_like_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
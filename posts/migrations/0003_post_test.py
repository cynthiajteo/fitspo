# Generated by Django 3.2.3 on 2021-05-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.TextField(default=False),
        ),
    ]
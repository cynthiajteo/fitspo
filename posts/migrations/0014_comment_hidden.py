# Generated by Django 3.2.3 on 2021-06-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]

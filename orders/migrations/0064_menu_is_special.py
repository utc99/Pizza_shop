# Generated by Django 2.2.1 on 2019-05-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0063_menu_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_special',
            field=models.IntegerField(default=0),
        ),
    ]

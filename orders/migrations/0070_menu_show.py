# Generated by Django 2.2.1 on 2019-05-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0069_remove_menu_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
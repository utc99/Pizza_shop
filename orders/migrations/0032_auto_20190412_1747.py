# Generated by Django 2.2 on 2019-04-12 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20190412_1738'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Customer2',
        ),
    ]

# Generated by Django 2.2 on 2019-04-04 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190404_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menupriority',
            old_name='topping_type',
            new_name='priority',
        ),
        migrations.RenameField(
            model_name='pizzatoppingstypes',
            old_name='priority',
            new_name='topping_type',
        ),
    ]

# Generated by Django 2.2 on 2019-04-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0039_order_orderlist2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderlist',
            new_name='dishes',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderlist2',
        ),
    ]
# Generated by Django 2.2 on 2019-04-04 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20190404_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='toppings',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.PizzaToppingsTypes'),
        ),
    ]

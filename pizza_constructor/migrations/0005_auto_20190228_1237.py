# Generated by Django 2.1.7 on 2019-02-28 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_constructor', '0004_remove_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderingredient',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='pizza_constructor.Order'),
        ),
    ]

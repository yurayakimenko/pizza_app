# Generated by Django 2.1.7 on 2019-02-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_constructor', '0005_auto_20190228_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]

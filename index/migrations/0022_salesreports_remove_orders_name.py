# Generated by Django 5.0.4 on 2024-04-18 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_remove_orders_image_remove_orders_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalSale', models.IntegerField(default=0)),
                ('totalProfit', models.IntegerField(default=0)),
                ('totalQuantity', models.IntegerField(default=0)),
                ('date_From', models.DateField(default=datetime.date(2021, 6, 15))),
                ('date_to', models.DateField(default=datetime.date(2021, 6, 15))),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
    ]

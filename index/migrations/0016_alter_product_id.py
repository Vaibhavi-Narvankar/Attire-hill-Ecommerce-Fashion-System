# Generated by Django 5.0.4 on 2024-04-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-03 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_rename_customer_email_contactform_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

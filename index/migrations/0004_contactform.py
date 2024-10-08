# Generated by Django 5.0.1 on 2024-04-03 06:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_category_colorvariant_product_productimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

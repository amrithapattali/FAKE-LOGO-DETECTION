# Generated by Django 5.0.3 on 2024-03-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-02 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_product_image_seller_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_verified',
        ),
    ]

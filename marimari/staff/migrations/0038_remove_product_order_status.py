# Generated by Django 4.0.4 on 2022-06-25 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0037_remove_cart_product_qty_product_order_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order_status',
        ),
    ]
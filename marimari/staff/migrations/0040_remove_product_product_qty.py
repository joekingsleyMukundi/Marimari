# Generated by Django 4.0.4 on 2022-06-25 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0039_alter_product_product_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_qty',
        ),
    ]

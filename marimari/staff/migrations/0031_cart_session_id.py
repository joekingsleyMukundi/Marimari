# Generated by Django 4.0.4 on 2022-06-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0030_alter_cart_product_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

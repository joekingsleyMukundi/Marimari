# Generated by Django 4.0.4 on 2022-06-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0032_customer_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user_cart',
            field=models.ManyToManyField(blank=True, related_name='user_cart', to='staff.customer'),
        ),
    ]
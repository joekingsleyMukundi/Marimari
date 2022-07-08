# Generated by Django 4.0.4 on 2022-06-06 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_product_user_cart_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.product')),
            ],
        ),
    ]
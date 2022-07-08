# Generated by Django 4.0.4 on 2022-06-06 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0013_alter_product_user_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_cart',
            field=models.ManyToManyField(blank=True, related_name='user_cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.product')),
            ],
        ),
    ]
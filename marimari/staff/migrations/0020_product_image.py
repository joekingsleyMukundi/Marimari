# Generated by Django 4.0.4 on 2022-06-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]

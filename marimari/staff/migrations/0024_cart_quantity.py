# Generated by Django 4.0.4 on 2022-06-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0023_productimage_image1_productimage_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

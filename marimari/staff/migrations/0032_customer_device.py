# Generated by Django 4.0.4 on 2022-06-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0031_cart_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

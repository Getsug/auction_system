# Generated by Django 4.0 on 2021-12-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_rename_mimimum_bid_productregistration_minimum_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='productregistration',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-10 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_productregistration_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productregistration',
            old_name='mimimum_bid',
            new_name='minimum_bid',
        ),
    ]

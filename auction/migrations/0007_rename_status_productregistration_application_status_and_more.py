# Generated by Django 4.0 on 2021-12-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_productregistration_auction_end_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productregistration',
            old_name='status',
            new_name='application_status',
        ),
        migrations.AddField(
            model_name='productregistration',
            name='auction_status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('EXPIRED', 'Expired'), ('WAITING', 'Waiting')], default='WAITING', max_length=10),
        ),
    ]

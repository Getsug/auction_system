# Generated by Django 4.0 on 2021-12-10 06:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_email', models.EmailField(max_length=254)),
                ('product', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('mimimum_bid', models.PositiveIntegerField()),
                ('auction_timespan', models.PositiveIntegerField()),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('seller_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
# Generated by Django 4.1.3 on 2023-05-02 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_order_state_profile_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='mobile',
        ),
    ]

# Generated by Django 4.1.3 on 2023-03-30 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_category_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='otp',
        ),
    ]
# Generated by Django 4.1.3 on 2023-05-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0028_remove_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payments',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(default='', max_length=150),
        ),
    ]

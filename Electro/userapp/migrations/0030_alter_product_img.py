# Generated by Django 4.1.3 on 2023-05-31 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0029_remove_order_payments_order_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
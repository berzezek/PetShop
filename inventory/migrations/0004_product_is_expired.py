# Generated by Django 4.0.4 on 2022-06-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]

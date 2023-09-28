# Generated by Django 3.2.19 on 2023-08-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_backend', '0015_cryptocurrency_sell_price_multiplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='id',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='priceupdate',
            name='id',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='priceupdate',
            name='price_time',
            field=models.JSONField(max_length=1000, null=True),
        ),
    ]
# Generated by Django 3.2.19 on 2023-06-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_backend', '0006_coins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coins',
            name='asset_platform_id',
        ),
        migrations.AlterField(
            model_name='coins',
            name='blockchain_site',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='coins',
            name='categories',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='coins',
            name='homepage',
            field=models.CharField(max_length=100),
        ),
    ]
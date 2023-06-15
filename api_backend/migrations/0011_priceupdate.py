# Generated by Django 3.2.19 on 2023-06-15 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_backend', '0010_auto_20230614_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_backend.coins')),
            ],
        ),
    ]

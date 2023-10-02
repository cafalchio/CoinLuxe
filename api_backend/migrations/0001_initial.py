# Generated by Django 3.2.19 on 2023-10-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.CharField(max_length=300,
                 primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('block_time_in_minutes',
                 models.PositiveIntegerField(default=0, null=True)),
                ('description', models.TextField(null=True)),
                ('homepage', models.JSONField(max_length=100, null=True)),
                ('blockchain_site', models.JSONField(max_length=100, null=True)),
                ('market_cap_rank', models.PositiveIntegerField(default=0)),
                ('categories', models.JSONField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.CharField(max_length=100,
                 primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(null=True)),
                ('current_price', models.FloatField(null=True)),
                ('market_cap', models.BigIntegerField(null=True)),
                ('market_cap_rank', models.PositiveIntegerField(null=True)),
                ('fully_diluted_valuation', models.BigIntegerField(null=True)),
                ('total_volume', models.BigIntegerField(null=True)),
                ('high_24h', models.FloatField(null=True)),
                ('low_24h', models.FloatField(null=True)),
                ('price_change_24h', models.FloatField(null=True)),
                ('price_change_percentage_24h', models.FloatField(null=True)),
                ('market_cap_change_24h', models.FloatField(null=True)),
                ('market_cap_change_percentage_24h', models.FloatField(null=True)),
                ('circulating_supply', models.FloatField(null=True)),
                ('total_supply', models.FloatField(null=True)),
                ('max_supply', models.FloatField(null=True)),
                ('ath', models.FloatField(null=True)),
                ('ath_change_percentage', models.FloatField(null=True)),
                ('ath_date', models.DateTimeField(null=True)),
                ('atl', models.FloatField(null=True)),
                ('atl_change_percentage', models.FloatField(null=True)),
                ('atl_date', models.DateTimeField(null=True)),
                ('last_updated', models.DateTimeField()),
                ('sell_price_multiplier', models.FloatField(default=1.001)),
            ],
            options={
                'ordering': ['-market_cap'],
            },
        ),
        migrations.CreateModel(
            name='PriceUpdate',
            fields=[
                ('id', models.CharField(max_length=300,
                 primary_key=True, serialize=False)),
                ('price_time', models.JSONField(max_length=1000, null=True)),
            ],
        ),
    ]

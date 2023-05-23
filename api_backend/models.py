from django.db import models


class CryptoCurrency(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    image = models.URLField(null=True)
    current_price = models.FloatField()
    market_cap = models.BigIntegerField()
    market_cap_rank = models.PositiveIntegerField()
    fully_diluted_valuation = models.BigIntegerField(null=True)
    total_volume = models.BigIntegerField()
    high_24h = models.FloatField()
    low_24h = models.FloatField()
    price_change_24h = models.FloatField()
    price_change_percentage_24h = models.FloatField()
    market_cap_change_24h = models.FloatField()
    market_cap_change_percentage_24h = models.FloatField()
    circulating_supply = models.FloatField(null=True)
    total_supply = models.FloatField(null=True)
    max_supply = models.FloatField(null=True)
    ath = models.FloatField()
    ath_change_percentage = models.FloatField()
    ath_date = models.DateTimeField()
    atl = models.FloatField()
    atl_change_percentage = models.FloatField()
    atl_date = models.DateTimeField(null=True)
    roi = models.JSONField(null=True)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name

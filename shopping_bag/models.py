from django.db import models
from django.contrib.auth.models import User


class Paid(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(
        "api_backend.CryptoCurrency", on_delete=models.CASCADE
    )
    amount = models.FloatField(null=True, default=0)

    @property
    def formatted_amount(self):
        if self.amount >= 1000:
            return f"{self.amount / 1000}K"
        elif self.amount >= 1000000:
            return f"{self.amount / 1000000}Mi"
        return self.amount


class Bag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    holdings = models.ManyToManyField(
        "api_backend.CryptoCurrency",
        through="Holding")
    class Meta:
        db_table = 'Bag'
        

class Holding(models.Model):
    shopping_bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(
        "api_backend.CryptoCurrency", on_delete=models.CASCADE
    )
    amount = models.FloatField(null=True, default=0)
    @property
    def formatted_amount(self):
        if self.amount >= 1000:
            return f"{self.amount / 1000}K"
        elif self.amount >= 1000000:
            return f"{self.amount / 1000000}Mi"
        return self.amount

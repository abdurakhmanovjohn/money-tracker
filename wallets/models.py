from django.conf import settings
from django.db import models

class Wallet(models.Model):
    WALLET_TYPE_CHOICES = (
        ("cash", "Cash"),
        ("card", "Card"),
    )

    CURRENCY_CHOICES = (
        ("UZS", "UZS"),
        ("USD", "USD"),
        ("EUR", "EUR"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallets")

    name = models.CharField(max_length=50, unique=True)
    wallet_type = models.CharField(max_length=10, choices=WALLET_TYPE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.currency})"
    

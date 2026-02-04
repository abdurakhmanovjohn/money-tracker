from django.conf import settings
from django.db import models

from wallets.models import Wallet
from categories.models import Category


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ("income", "Income"),
        ("expense", "Expense"),
        ("transaction_in", "Transaction In"),
        ("transaction_out", "Transaction Out")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions",)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,)

    type = models.CharField(max_length=15, choices=TRANSACTION_TYPE_CHOICES,)
    amount = models.DecimalField(max_digits=14, decimal_places=2,)
    exchange_rate = models.DecimalField(max_digits=14, decimal_places=4, null=True, blank=True,)

    related_transaction = models.OneToOneField("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_transaction",)

    note = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount} {self.wallet.currency}"


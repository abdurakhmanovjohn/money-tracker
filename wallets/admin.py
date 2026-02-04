from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "wallet_type", "currency", "balance",)
    list_filter = ("wallet_type", "currency")
    search_fields = ("name", "user__phone_number")

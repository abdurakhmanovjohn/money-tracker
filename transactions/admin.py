from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "wallet", "amount", "date")
    list_filter = ("type", "wallet__currency")
    search_fields = ("note",)
    date_hierarchy = "date"
from django.conf import settings
from django.db import models

class Category(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="categories")

    type = models.CharField(max_length=7, choices=CATEGORY_TYPE_CHOICES)

    name_en = models.CharField(max_length=50)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name_en} ({self.type})"

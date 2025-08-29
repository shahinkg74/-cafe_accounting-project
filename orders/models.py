from django.db import models
from django.utils import timezone
from django.conf import settings
from menu.models import MenuItem
from datetime import datetime
from decimal import Decimal


class Order(models.Model):
    created_at = models.DateField(default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"سفارش#{self.id} - {self.created_at.strftime('%Y/%m/%d')}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))

    def total_price(self):
        return self.quantity * self.item_price

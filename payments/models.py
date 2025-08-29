from django.contrib.auth import get_user_model
from django.db import models
from menu.models import MenuItem

User = get_user_model()


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'نقدی'),
        ('card', 'کارت بانکی'),
        ('online', 'آنلاین'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'پرداخت #{self.id} - {self.total_amount} ریال'


class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_subtotal(self):
        return self.quantity * self.price

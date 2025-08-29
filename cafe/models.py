from django.db import models
from django.utils import timezone
# from menu.models import MenuItem


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


# class Order(models.Model):
#     items = models.ManyToManyField(MenuItem)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)
#     timestamp = models.DateTimeField(default=timezone.now)
#

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

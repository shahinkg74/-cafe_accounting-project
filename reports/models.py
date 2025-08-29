from django.db import models


class DailyReport(models.Model):
    date = models.DateField(unique=True)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"گزارش روز {self.date}"

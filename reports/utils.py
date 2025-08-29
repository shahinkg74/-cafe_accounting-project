from orders.models import Order
from datetime import date


def calculate_daily_report(report_date=None):
    report_date = report_date or date.today()
    orders = Order.objects.filter(created_at=report_date)

    total_sales = sum(order.total_price for order in orders)
    total_cost = sum(order.total_cost for order in orders)
    profit = total_sales - total_cost

    return {
        'total_sales': total_sales,
        'total-cost': total_cost,
        'profit': profit,
    }

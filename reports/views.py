from django.shortcuts import render
from decimal import Decimal
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date
from .models import DailyReport
from .utils import calculate_daily_report


def is_manager(user):
    return user.role == 'manager'


# @login_required
# @user_passes_test(is_manager)
def daily_report_view(request):
    today = date.today()
    daily_report, create = DailyReport.objects.get_or_create(date=today)
    report_data = calculate_daily_report()

    daily_report.total_sales = report_data.get('total_sale', 0)
    daily_report.total_cost = report_data.get('total_cost', 0)
    daily_report.total_profit = report_data.get('profit', 0)
    daily_report.save()

    context = {
        'daily_report': daily_report,
    }
    return render(request, 'reports/daily_report.html',context)

from django.shortcuts import render, redirect
from django.db import models
from django.utils.timezone import now
from datetime import date
from .models import MenuItem, Expense
from orders.models import Order


def dashboard(request):
    today = date.today()

    recent_orders = Order.objects.order_by('-created_at')[:10]

    todays_sales = (
            Order.objects.filter(created_at=today, paid=True)
            .aggregate(total=models.Sum('total_price'))['total']
            or 0
    )

    todays_expenses = (
            Expense.objects.filter(timestamp=today)
            .aggregate(total=models.Sum('amount'))['total']
            or 0
    )

    profit = todays_sales - todays_expenses

    context = {
        "recent_orders": recent_orders,
        "todays_sales": todays_sales,
        "todays_expenses": todays_expenses,
        "profit": profit,
    }
    return render(request, "cafe/dashboard.html", context)


# def dashboard(request):
#     today = now().date()
#     income = Order.objects.filter(created_at__date=date.today().aggregate(sum=Sum('total_price'))['sum'] or 0
#     cost = Expense.objects.filter(created_at__date=date.today().aggregate(sum=Sum('amount'))['sum'] or 0
#     profit = income - cost
#     return render(request, 'cafe/dashboard.html', {'income': income, 'cost': cost, 'profit': profit})


# def add_order(request):
#     if request.method == 'POST':
#         item_ids = request.POST.getlist('items')
#         items = MenuItem.objects.filter(id__in=item_ids)
#         total = sum(item.price for item in items)
#         order = Order.objects.create(total_price=total)
#         order.items.set(items)
#         return redirect('dashboard')
#
#     menu = MenuItem.objects.all()
#     return render(request, 'cafe/add_order.html', {'menu': menu})


def add_expense(request):
    if request.method == 'POST':
        desc = request.POST['description']
        amt = request.POST['amount']
        Expense.objects.create(description=desc, amount=amt)
        return redirect('dashboard')
    return render(request, 'cafe/add_expense.html')

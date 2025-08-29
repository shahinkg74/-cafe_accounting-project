from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderItemFormSet
from .models import Order
from django.contrib import messages


# @login_required()
def create_order(request):
    if request.method == 'POST':
        formset = OrderItemFormSet(request.POST)
        if formset.is_valid():
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,)
            total_price = 0
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    item = form.save(commit=False)
                    item.order = order
                    item.item_price = item.menu_item.price
                    item.cost_price = item.menu_item.cost_price
                    item.save()
                    total_price += item.item_price * item.quantity
            order.total_price = total_price
            order.save()
            messages.success(request, 'سفارش با موفقیت ثبت شد.')
            return redirect('order:list')

    else:
        formset = OrderItemFormSet()

    return render(request, 'order_form.html', {'formset': formset})


def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})


def print_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'print_order.html', {'order': order})

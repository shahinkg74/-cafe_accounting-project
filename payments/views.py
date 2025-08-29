from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Payment, PaymentItem
from .forms import PaymentForm
from menu.models import MenuItem
from inventory.models import InventoryItem
from django.db import transaction
from django.utils import timezone


def is_cashier(user):
    return user.role == 'cashier'


# @login_required
# @user_passes_test(is_cashier)
def create_payment(request):
    menu_items = MenuItem.objects.filter(is_availabel=True)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        items = request.POST.getlist('items[]')
        quantities = request.POST.getlist('quantities[]')
        if form.is_valid() and items and quantities and len(items) == len(quantities):
            with transaction.atomic():
                total = 0
                payment = form.save(commit=False)
                payment.user = request.user
                payment.total_amount = 0
                payment.save()

                for item_id, qty in zip(items, quantities):
                    menu_item = MenuItem.objects.get(id=item_id)
                    qty = int(qty)
                    PaymentItem.objects.create(
                        paymnet=payment,
                        menu_item=menu_item,
                        quantity=qty,
                        price=menu_item.price
                    )
                    try:
                        inv_item = InventoryItem.objects.get(name=menu_item.name)
                        inv_item.quantity -= qty
                        if inv_item.quantity < 0:
                            raise ValueError('موجودی انبار کافی نیست')
                        inv_item.save()
                    except InventoryItem.DoesNotExist:
                        # age kala dar anbar mojud nabud  hoshdar midahim
                        pass

                    total += menu_item.price * qty

                payment.total_amount = total
                payment.save()
            return redirect('payments:payment_detail', pk=payment.pk)
        else:
            form = PaymentForm()
        return render(request, 'payments/payment_form.html', {'from': form})


def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payments/payment_detail.html', {'payment': payment})


def payment_list(request):
    payments = Payment.objects.all().order_by('-date')
    total_amount = sum(p.total_amount for p in payments)
    context = {
        'payments': payments,
        'total_amount': total_amount,
        'today': timezone.now().date()
    }
    return render(request, 'payments/payment_list.html', context)
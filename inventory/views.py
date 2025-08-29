from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import InventoryItem
from .forms import InventoryItemForm


def is_manager_or_stock(request, user):
    return getattr(user, 'role', None) in ['manager', 'stock']


# @login_required
# @user_passes_test(is_manager_or_stock)
def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})


# @login_required
# @user_passes_test(is_manager_or_stock)
def inventory_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/inventory_form.html', {'form': form})


# @login_required
# @user_passes_test(is_manager_or_stock)
def inventory_update(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory:list')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'inventory/inventory_form.html', {'form': form})

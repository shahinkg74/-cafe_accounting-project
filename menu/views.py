from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, MenuItem
from .forms import CategoryForm, MenuItemForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.role == 'manager'


# @user_passes_test(is_manager)


# @login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/category_list.html', {'categories': categories})


# @login_required
# @user_passes_test(is_manager)
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:category_list')
    else:
        form = CategoryForm()
    return render(request, 'menu/category_from.html', {'form': form})


# @login_required
# @user_passes_test(is_manager)
def menuitem_list(request):
    items = MenuItem.objects.select_related('category').all()
    return render(request, 'menu/menuitem_list.html', {'items': items})


# @login_required
# @user_passes_test(is_manager)
def menuitem_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:menuitem_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu/menuitem_form.html', {'form': form})

from django import forms
from .models import Category, MenuItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name: نام دسته بندی'}


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'cost_price', 'category', 'is_available']
        labels = {
            'name': 'نام محصول',
            'description': 'توضیحات',
            'price': 'قیمت فروش',
            'cost_price': 'قیمت تمام شده',
            'category': 'دسته بندی',
            'is_available': 'موجود است؟',

        }

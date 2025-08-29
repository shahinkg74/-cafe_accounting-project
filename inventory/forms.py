from django import forms
from .models import InventoryItem


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'unit', 'min_quantity']
        labels = {
            'name': 'نام کالا',
            'quantity': 'مقدار موجود',
            'unit': 'واحد',
            'min_quantity': 'حداقل مقدرا هشدار',
        }

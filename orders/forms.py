from django import forms
from .models import Order, OrderItem
from menu.models import MenuItem


class OrderItemForm(forms.ModelForm):
    menu_item = forms.ModelChoiceField(queryset=MenuItem.objects.filter(is_available=True), label="محصول")
    quantity = forms.IntegerField(min_value=1, initial=1, label="تعداد")

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']


OrderItemFormSet = forms.inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1, can_delete=True)

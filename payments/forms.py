from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['method', 'notes']
        labels = {
            'method': 'روش پرداخت',
            'notes': 'یادداشت ها',
        }

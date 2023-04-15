# django imports
from django import forms

# app imports
from portfolio.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []

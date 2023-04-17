# django imports
from django.db.models import Sum
from django import forms
from django.core.exceptions import ValidationError

# app imports
from portfolio.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        order_type = cleaned_data.get('order_type')

        if order_type == Order.SELL:
            # don't sell shares that you don't have
            asset = cleaned_data.get('asset')
            amount = cleaned_data.get('amount')
            amount_bought = asset.orders.filter(order_type=Order.BUY)\
                                        .aggregate(total_amount=Sum('amount'))
            amount_sold = asset.orders.filter(order_type=Order.SELL)\
                                      .aggregate(total_amount=Sum('amount'))

            amount_bought = amount_bought['total_amount'] or 0
            amount_sold = amount_sold['total_amount'] or 0
            current_amount = amount_bought - amount_sold

            if current_amount - amount < 0:
                raise ValidationError('Cannot sell shares you don\'t have')

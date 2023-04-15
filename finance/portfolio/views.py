# python imports
from decimal import Decimal

# django imports
from django.db import models
from django.db.models import Sum, F
from django.shortcuts import render, redirect

# app imports
from portfolio.models import Asset, Order
from portfolio.forms import OrderForm


def portfolio(request):
    # retrieve portfolio assets
    asset_ids = Order.objects.values_list('asset_id', flat=True).distinct()
    assets = Asset.objects.filter(id__in=asset_ids)

    # initialize portfolio data
    positions =  []
    portfolio_value = Decimal('0')
    portfolio_unrealised_gains = Decimal('0')
    portfolio_invested = Decimal('0')

    for asset in assets:
        # retrieve buy / sell orders for each asset
        buy_orders = asset.orders.filter(order_type=Order.BUY)
        sell_orders = asset.orders.filter(order_type=Order.SELL)
        
        buy_data = buy_orders.aggregate(total_amount=Sum('amount'),
                                        total_value=Sum(F('price') * F('amount')))
        
        sell_data = sell_orders.aggregate(total_amount=Sum('amount'),
                                          total_value=Sum(F('price') * F('amount')))
        
        # calculate remaining amount after buy / sell orders
        amount_bought = buy_data['total_amount'] or 0
        amount_sold = sell_data['total_amount'] or 0
        current_amount = amount_bought - amount_sold

        # calculate the total cost of all buy / sell orders
        value_bought = buy_data['total_value'] or 0
        value_sold = sell_data['total_value'] or 0
        
        # calculate the current valuation
        last_price = asset.prices.latest('day')
        current_valuation = current_amount * last_price.price

        # calculate unrealised gains
        cost_basis_per_unit = value_bought / amount_bought
        total_cost_basis = (current_amount * cost_basis_per_unit) + value_sold
        unrealised_gains = current_valuation - total_cost_basis

        positions.append({
            'asset': asset,
            'amount': current_amount,
            'price': last_price.price,
            'valuation': current_valuation,
            'unrealised_gains': unrealised_gains
        })

        portfolio_value += current_valuation
        portfolio_unrealised_gains += unrealised_gains
        portfolio_invested += value_bought - value_sold
    
    return render(request, 'portfolio.html', locals())


def order_list(request):
    orders = Order.objects.order_by('-day')
    return render(request, 'order/list.html', {'orders': orders})


def order_create(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('portfolio')
    return render(request, 'order/create.html', {'form': form})

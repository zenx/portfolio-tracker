# django imports
from django.contrib import admin

# project imports
from portfolio.models import Asset, Price, Order


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'name']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['asset', 'day', 'price']
    date_hierarchy = 'day'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['day', 'order_type', 'amount', 'asset', 'price', 'day']
    list_filter = ['order_type', 'day']
    date_hierarchy = 'day'

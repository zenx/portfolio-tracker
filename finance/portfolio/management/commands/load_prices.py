# python imports
import requests
import datetime

# django imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# project imports
from portfolio.models import Asset, Price


class Command(BaseCommand):
    help = 'Loads asset end of day prices from Marketstack'

    def handle(self, *args, **options):
        # set up the API endpoint URL and parameters
        endpoint = 'http://api.marketstack.com/v1/eod/latest'
        symbols = Asset.objects.values_list('ticker', flat=True)

        # make the API request and get the JSON response
        response = requests.get(endpoint,
                                params={'access_key': settings.MARKETSTACK_API_KEY,
                                        'symbols': ','.join(symbols)})
        json_response = response.json()
        
        for data in json_response['data']:
            asset = Asset.objects.get(ticker=data['symbol'])
            day = datetime.datetime.fromisoformat(data['date']).date()

            try:
                # check if price already exists
                price = Price.objects.get(asset=asset,
                                          day=day)
            except Price.DoesNotExist:
                price = Price.objects.create(asset=asset,
                                             day=day,
                                             price=data['adj_close'])
            
                print(f'Price for {asset.ticker} on {day} created')
            else:
                print(f'Price for {asset.ticker} on {day} already exists')
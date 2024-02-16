import requests

from datetime import datetime

from django.core.management.base import BaseCommand

from currency.models import Currency


ENDPOINT = 'https://www.cbr-xml-daily.ru/daily_json.js'


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            currency_data = requests.get(ENDPOINT)
        except Exception as error:
            raise Exception(f'Ошибка при запросе к API ЦБ: {error}')
        response = currency_data.json()
        datetime_string = response['Date']
        date_time = datetime.fromisoformat(datetime_string)
        date = date_time.date()
        currencies = []
        for valute, data in response['Valute'].items():
            currencies.append(
                    Currency(
                        name=data.get('Name'),
                        charcode=valute,
                        date=date,
                        rate=data.get('Value'),
                    )
                )
        Currency.objects.bulk_create(currencies)

import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')
        
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try: 
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать валюту {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}&api_key={"903d325cd8aa165d9d51e09bc94ff2f1fff1401b06bed64ba2d17a1953aa5beb"}')

        total_base = json.loads(r.content)[base_ticker]

        return total_base
# api_wrapper.py
# Integrates and standardizes the APIs to provide a more uniform approach for other parts of the app
# Ahmed Kamal
# October 25 2021


from coinbase.wallet.client import Client as CoinbaseClient
from bittrex.bittrex import Bittrex as BittrexClient
import json
import time


class ExchangeAPIWrapper():

    def __init__(self, symbols=["BTC","ETH"]):
        config_data = open("config.json")
        config_data = json.load(config_data)
        self.b_client = BittrexClient(None, None)
        self.c_client = CoinbaseClient(config_data["Coinbase_API_Key"], config_data["Coinbase_API_Secret"], api_version=config_data["Coinbase_API_Version"])
        self.b_data = {"Exchange": "Bittrex"}
        self.c_data = {"Exchange": "Coinbase"}
        self.symbols = symbols
        for symbol in self.symbols:
            self.b_data[symbol] = {"Buy": -1, "Sell": -1}
            self.c_data[symbol] = {"Buy": -1, "Sell": -1}
        self.exchange_data = [self.b_data, self.c_data]
        self.update_and_get_prices()

    def update_and_get_prices(self):
        # TODO: Write error handling for failure to return data from APIs
        for symbol in self.symbols:
            temp = self.b_client.get_ticker(f"USD-{symbol}")
            self.b_data[symbol]["Sell"] = temp["result"]["Bid"]
            self.b_data[symbol]["Buy"] = temp["result"]["Ask"]
            self.c_data[symbol]["Buy"] = self.c_client.get_buy_price(currency_pair = f'{symbol}-USD')["amount"]
            self.c_data[symbol]["Sell"] = self.c_client.get_sell_price(currency_pair = f'{symbol}-USD')["amount"]
        return self.exchange_data


def test():
    e = ExchangeAPIWrapper()
    print(e.update_and_get_prices())
    time.sleep(10)
    print(e.update_and_get_prices())
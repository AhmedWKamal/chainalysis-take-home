# backend.py
# Access Exchange data periodically and store it in our database
# Ahmed Kamal
# October 25 2021


import time
import api_wrapper
import threading


class Backend():

    def __init__(self, symbols=["BTC","ETH"]):
        self.exchanges = api_wrapper.ExchangeAPIWrapper(symbols)
        self.data = self.exchanges.update_and_get_prices()
        self.update_time = time.strftime("%H:%M:%S", time.localtime())
        self.data.append(self.update_time)
        thread = threading.Thread(target=self.update_data, args=())
        thread.daemon = True
        thread.start()

    def update_data(self):
        while True:
            self.data = self.exchanges.update_and_get_prices()
            self.data.append(time.strftime("%H:%M:%S", time.localtime()))
            self.write_to_database()
            time.sleep(3)

    def get_raw_data(self):
        return self.data
    
    def get_formatted_string_data(self):
        return str(self.data)

    def write_to_database(self):
        #TODO: Connect and write to a hosted database
        # Will actually write to a file here
        f = open("data.txt", "w")
        f.write(str(self.data)+"\n")
        f.close()
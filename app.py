from flask import Flask, jsonify, render_template
import backend as be

app = Flask(__name__)

@app.route("/")
def home():
    # Start our backend server
    mybackend = be.Backend()
    a,b,c,d,e = update_prices()
    return render_template('index.html', bittrex_BTC_price=a, coinbase_BTC_price=b,bittrex_ETH_price=c,coinbase_ETH_price=d,current_time=e)

def update_prices():
    f = open("data.txt", "r")
    bittrex_BTC_prices = []
    bittrex_ETH_prices = []
    coinbase_BTC_prices = []
    coinbase_ETH_prices = []
    final_timestamp = None
    for line in f:
        data = eval(line)
        bittrex_BTC_prices.append(float(data[0]["BTC"]["Buy"]))
        bittrex_ETH_prices.append(float(data[0]["ETH"]["Buy"]))
        coinbase_BTC_prices.append(float(data[1]["BTC"]["Buy"]))
        coinbase_ETH_prices.append(float(data[1]["ETH"]["Buy"]))
        final_timestamp = data[2]
    bittrex_BTC_price=bittrex_BTC_prices[-1]
    coinbase_BTC_price=coinbase_BTC_prices[-1]
    bittrex_ETH_price=bittrex_ETH_prices[-1]
    coinbase_ETH_price=coinbase_ETH_prices[-1]
    current_time=final_timestamp
    return (bittrex_BTC_price,coinbase_BTC_price,bittrex_ETH_price,coinbase_ETH_price,current_time)

@app.route('/_update_page')
def update_page():
    bittrex_BTC_price,coinbase_BTC_price,bittrex_ETH_price,coinbase_ETH_price,current_time = update_prices()
    return jsonify(bittrex_BTC_price,coinbase_BTC_price,bittrex_ETH_price,coinbase_ETH_price,current_time)
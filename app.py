from flask import Flask, jsonify, render_template
import backend as be
import json
app = Flask(__name__)

@app.route("/")
def home():
    # Start our backend server
    mybackend = be.Backend()
    data = update_prices()
    return render_template('index.html', data=data)

def update_prices():
    #bittrex_BTC_prices.append(float(data[0]["BTC"]["Buy"]))
    f = open("data.txt", "r")
    data = eval(f.readline())
    return (data)

@app.route('/_update_page')
def update_page():
    data = update_prices()
    return jsonify(json.dumps(data))
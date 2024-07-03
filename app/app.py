"""
A simple Flask app to greet visitors.
"""
from flask import Flask
import os
import random

app = Flask(__name__)

"""
Display Price
"""
@app.route("/")
def ethPrice():
    price = random.randint(2200000, 3300000)/100
    price_string = str(price)
    return "The current price of Ethereum is: " + price_string

@app.route("/nvidia")
def nvdaPrice():
    price = random.randint(11000, 16000)/100
    price_string = str(price)
    return "The current price of NVIDIA is: " + price_string

@app.route("/release")
def releaseVersion():
    return "Release V1.0.0"


"""
Runtime
"""
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

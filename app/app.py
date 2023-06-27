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
def price():
    price = random.randint(2500000, 3500000)/100
    price_string = str(price)
    return "The price of Bitcoin is: " + price_string

"""
Runtime
"""
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

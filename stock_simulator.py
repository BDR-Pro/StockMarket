from flask import Flask, request, jsonify
app = Flask(__name__)

# Initial stock data: price, and available quantity.
stock_data = {
    'price': 100.0,
    'quantity': 1000
}

def adjust_price(action, amount):
    """Adjust the stock price based on buy/sell action and amount."""
    price_change = 0.01  # Price change factor per share.
    if action == 'buy':
        stock_data['price'] += price_change * amount
        stock_data['quantity'] -= amount
    elif action == 'sell':
        stock_data['price'] -= price_change * amount
        stock_data['quantity'] += amount
    # Ensure the price doesn't go below some minimal value.
    stock_data['price'] = max(1.0, stock_data['price'])

@app.route('/buy', methods=['POST'])
def buy():
    """Endpoint to buy stock."""
    amount = request.json.get('amount', 0)
    adjust_price('buy', amount)
    return jsonify({'status': 'success', 'new_price': stock_data['price'], 'quantity_left': stock_data['quantity']})

@app.route('/sell', methods=['POST'])
def sell():
    """Endpoint to sell stock."""
    amount = request.json.get('amount', 0)
    adjust_price('sell', amount)
    return jsonify({'status': 'success', 'new_price': stock_data['price'], 'quantity_added': stock_data['quantity']})

@app.route('/stock', methods=['GET'])
def stock():
    """Endpoint to check the current stock price and quantity."""
    return jsonify(stock_data)

@app.route('/', methods=['GET'])
def home():
    """Home page."""
    return 'Welcome to the stock trading app!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

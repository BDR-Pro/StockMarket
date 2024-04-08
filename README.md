# Simple Stock Market Simulator

This is a basic stock market simulator built with Flask for educational purposes. It simulates buying and selling a single stock, where each action affects the stock's price. The simulator includes three main operations: buying stock, selling stock, and checking the stock's current price and available quantity.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Flask

### Installation

First, install Flask using pip if you haven't already:

```bash
pip install Flask
```

### Running the Simulator

1. Clone this repository or download the `stock_simulator.py` file.
2. Navigate to the directory containing `stock_simulator.py`.
3. Run the simulator using the following command:

```bash
python stock_simulator.py
```

The simulator will start running on `http://localhost:5000`.

## API Endpoints

- **Buy Stock**: `/buy` (POST)
- **Sell Stock**: `/sell` (POST)
- **Check Stock**: `/stock` (GET)

### Using `curl` to Interact with the Simulator

**Buying Stock:**

To buy a quantity of stock, use the `/buy` endpoint with a POST request. Replace `amount` with the number of shares you wish to purchase.

```bash
curl -X POST http://localhost:5000/buy -H "Content-Type: application/json" -d '{"amount": 10}'
```

**Selling Stock:**

To sell a quantity of stock, use the `/sell` endpoint with a POST request. Replace `amount` with the number of shares you wish to sell.

```bash
curl -X POST http://localhost:5000/sell -H "Content-Type: application/json" -d '{"amount": 5}'
```

**Checking Stock Price and Quantity:**

To check the current stock price and available quantity, use the `/stock` endpoint with a GET request.

```bash
curl http://localhost:5000/stock
```

## Note

This simulator is a simplified representation designed for educational purposes. Real-world trading systems involve more complex considerations such as market liquidity, transaction security, and regulatory compliance.

----
<video controls src="stockmarket.mp4" title="Title"></video>
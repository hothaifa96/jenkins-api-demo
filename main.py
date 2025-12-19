from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Data set of 30 major currencies (Rate relative to 1 USD)
# These are approximate values for demonstration
rates = {
    "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "ILS": 3.65, "JPY": 150.25,
    "AUD": 1.53, "CAD": 1.35, "CHF": 0.88, "CNY": 7.19, "HKD": 7.82,
    "NZD": 1.62, "SEK": 10.45, "KRW": 1335.50, "SGD": 1.34, "NOK": 10.55,
    "MXN": 17.05, "INR": 82.95, "RUB": 92.40, "ZAR": 19.10, "TRY": 31.05,
    "BRL": 4.97, "TWD": 31.50, "DKK": 6.85, "PLN": 3.98, "THB": 35.85,
    "IDR": 15650.0, "HUF": 360.20, "CZK": 23.45, "AED": 3.67, "SAR": 3.75
}

@app.route('/api/rates', methods=['GET'])
def get_all_rates():
    """Returns the full list of 30 currencies and their current rates."""
    return jsonify({"base": "USD", "rates": rates})

@app.route('/api/convert', methods=['GET'])
def convert():
    """
    Path for amount change.
    Usage: /api/convert?from=USD&to=ILS&amount=100
    """
    from_curr = request.args.get('from', 'USD').upper()
    to_curr = request.args.get('to', 'ILS').upper()
    try:
        amount = float(request.args.get('amount', 1))
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

    if from_curr not in rates or to_curr not in rates:
        return jsonify({"error": "Currency not supported"}), 404

    # Calculation: (Amount / FromRate) * ToRate
    # We convert to USD first (base), then to the target
    converted_amount = (amount / rates[from_curr]) * rates[to_curr]
    
    return jsonify({
        "from": from_curr,
        "to": to_curr,
        "original_amount": amount,
        "converted_amount": round(converted_amount, 2),
        "rate": round(rates[to_curr] / rates[from_curr], 4)
    })

if __name__ == '__main__':
    app.run(debug=True , host="0.0.0.0", port=5005)
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY =  # Replace with your actual API key

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head>
    <title>USD to INR Converter</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
        }
        .converter-container {
            text-align: center;
            background: white;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
        }
        input[type="number"], button {
            padding: 10px;
            margin-top: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            width: calc(100% - 22px);
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        .error, .info {
            color: red;
            margin-top: 10px;
        }
        .info {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="converter-container">
        <h1>I'm your Daily Converter 😉💰</h1>
        <h2>Convert USD to INR</h2>
        <form method="post">
            <label>Amount in USD:</label>
            <input type="number" name="amount" step="0.01" required>
            <button type="submit">Convert</button>
        </form>

        {% if result is not none %}
            <h3>{{ amount }} USD = {{ result }} INR</h3>
            <p class="info">Current Conversion Rate: 1 USD = {{ rate }} INR</p>
        {% elif error %}
            <p class="error">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def convert():
    result = None
    error = None
    amount = None
    rate = None  # Initialize rate

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            url = 'https://anyapi.io/api/v1/exchange/convert'
            params = {
                'apiKey': API_KEY,
                'base': 'USD',
                'to': 'INR',
                'amount': amount
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                result = data.get('converted')
                if result is not None:
                    rate = result / amount  # Calculate rate if not provided
            else:
                error = f"API Error: {response.status_code}"
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template_string(HTML_TEMPLATE, result=result, amount=amount, error=error, rate=rate)

if __name__ == '__main__':
    app.run(debug=True)

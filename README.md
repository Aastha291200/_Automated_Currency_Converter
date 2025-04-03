
# 💱 Automated Currency Converter

A simple web-based USD to INR currency converter built with Flask and powered by the [AnyAPI](https://anyapi.io/) exchange rate API.

## Features

- Convert US Dollars (USD) to Indian Rupees (INR)
- Fetches real-time exchange rates using the AnyAPI
- Clean and responsive user interface
- Displays both the converted amount and current conversion rate

## Tech Stack

- Python
- Flask
- HTML/CSS
- AnyAPI for currency conversion data


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aastha291200/_Automated_Currency_Converter.git
   cd automated_currency_converter

## Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the dependencies:
pip install flask requests

## Replace the API key:
### Open app.py and replace the placeholder API key with your own from AnyAPI.
API_KEY = 'your_actual_api_key_here'

## Run the app:
python app.py

## Visit in your browser:
http://127.0.0.1:5000/

## Example
Enter an amount in USD, hit Convert, and see how much it's worth in INR with the current exchange rate!

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License
This project is licensed under the MIT License.

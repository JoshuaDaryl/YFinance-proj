from flask import Flask, render_template, url_for, request, redirect
from tickerlist import tickerList
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        user_input = request.form['symbol']
        user_input = user_input.upper()
        if user_input in tickerList:
            price = get_current_price(user_input).round(2)
            yahoo_finance_link = f"https://uk.finance.yahoo.com/quote/{user_input}"
            return render_template('index.html', price=price, yahoo_finance_link=yahoo_finance_link)
        else:
            notInIndex = "Sorry that stock is not is listed"
            return render_template('index.html', notInIndex = notInIndex)
    else:
        return render_template('index.html')

# Get current stock price
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

if __name__ == "__main__":
    app.run(port=8000, debug=True)

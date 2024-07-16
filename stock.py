import yfinance as yf
from tickerlist import get_tickers


#User selects price to recieve

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]



while True:
    userInput = input("Please enter ticker of stock you want: ")
    userInput = userInput.upper()
    if userInput in get_tickers:
        print(f"Current Price: {get_current_price(userInput).round(2)}")
        website = f"More info available @ https://uk.finance.yahoo.com/quote/" + userInput
        print(website)

    else:
        print("Please enter a valid ticker")

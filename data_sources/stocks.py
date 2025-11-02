import yfinance as yf

def get_current_price(ticker: str) -> float:
    """
    Returns the current closing price for the given ticker from Yahoo Finance.
    """
    try:
        etf = yf.Ticker(ticker)
        current_price = etf.history(period="1d")["Close"].iloc[-1]
        return float(current_price)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

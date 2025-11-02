from data_sources.stocks import get_current_price

def main():
    ticker = "ACWI"
    price = get_current_price(ticker)
    if price:
        print(f"Current price of ETF {ticker}: {price:.2f} USD")
    else:
        print("Failed to fetch the ETF price.")

if __name__ == "__main__":
    main()

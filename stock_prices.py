from googlefinance import getQuotes
import json

stocks = ["AAPL", "GOOG", "TSLA"]

print(json.dumps(getQuotes(stocks), indent = 2))
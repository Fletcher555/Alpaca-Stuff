

import alpaca_trade_api as tradeapi
import time


apiPublicKey = 'PKFO1HKRRFY8ADDND4WG'
apiPrivateKey = 'AwihaCN5bOr7H5iP6T5kpbjPZxHADDKbHQxPQjI4'
alpacaEndPoint = 'https://paper-api.alpaca.markets'
stock = ['GME', 'TSLA', 'CCJ', 'SPY', 'AAPL', 'MSFT', 'FB', 'NVDA', 'GOOG', 'BB', 'AMC', 'PLTR', 'DASH', 'MMM', 'DIS', 'KO']

# instantiate REST API
api = tradeapi.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')


def getStockData(stock):
    stockData = api.get_barset(stock, 'minute', limit = 3).df
    stockData.columns = stockData.columns.to_flat_index()
    stockData.columns = [x[1] for x in stockData.columns]
    stockData.reset_index(inplace=True)

    return stockData

def processData(stockData):
    if(stockData.open[0] < stockData.open[1] and stockData.open[1] < stockData.open[2]):
        return 'buy'
    elif(stockData.open[0] > stockData.open[1] and stockData.open[1] > stockData.open[2]):
        return 'sell'
    else:
        return 'hold'

def orderPlace(buySellHold, stockData , stock):
    if(buySellHold == 'buy'):
        api.submit_order(symbol = stock, qty=2, side = 'buy', type = 'market', time_in_force = 'day')
        return "buy"
    elif(buySellHold == 'sell'):
        api.submit_order(symbol=stock, qty=2, side='sell', type='market', time_in_force='day')
        return "sell"
    elif(buySellHold == 'hold'):
        return "hold"
    else:
        return "fail"


def goTimeBaby():
    marketStatus = api.get_clock()
    while(marketStatus.is_open == True):
        for x in range (16):
            stockData = getStockData(stock[x])
            buySellHold = processData(stockData)
            result = orderPlace(buySellHold, getStockData, stock[x])
            print(stock[x])
            print(result)
            time.sleep(1)
        time.sleep(60)

    print("Market Closed ):")

goTimeBaby()


import alpaca_trade_api as tradeapi
import time


apiPublicKey = 'PKSUP0209BL51C1WNTZQ'
apiPrivateKey = '72ZkhXTWuU6BePsKKku9KzNdYEu3sQd0u205d6jn'
alpacaEndPoint = 'https://paper-api.alpaca.markets'
stock = ['GME', 'TSLA', 'CCJ', 'SPY', 'AAPl', 'MSFT', 'FB', 'NVDA', 'GOOG', 'BB', 'AMC', 'PLTR', 'DASH', 'WEED', 'DIS', 'KO']

# instantiate REST API
api = tradeapi.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')


def getStockData(stock, x):
    stockData = api.get_barset(stock[x], 'minute', limit=3).df
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

def orderPlace(buySellHold, stockData , x):
    if(buySellHold == 'buy'):
        if(api.get_account().cash > 10 * stockData.close[2]):
            api.submit_order(symbol = stock[x], qty=10, side = 'buy', type = 'market', time_in_force = 'day')
            return "buy"
    elif(buySellHold == 'sell'):
        api.submit_order(symbol=stock[x], qty=10, side='sell', type='market', time_in_force='day')
        return "sell"
    elif(buySellHold == 'hold'):
        return "hold"
    else:
        return "fail"


def goTimeBaby():
    marketStatus = api.get_clock()
    while(marketStatus == 'open'):
        for x in range (15):
            stockData = getStockData(stock[x] , x)
            buySellHold = processData(stockData)
            result = orderPlace(buySellHold, getStockData, x)
            time.sleep(60)
        print(result)
    print("Market Closed ):")

goTimeBaby()
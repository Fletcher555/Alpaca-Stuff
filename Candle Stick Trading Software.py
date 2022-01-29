<<<<<<< HEAD
from yahoo_fin import options
import alpaca_trade_api as api
import apiClass
import time
import pandas as pd

apiPublicKey = apiClass.ApiCodes.apiPublic
apiPrivateKey = apiClass.ApiCodes.apiPrivate
alpacaEndPoint = apiClass.ApiCodes.apiLink
stockDataFile = pd.read_csv('top500Stocks')

api = api.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')

active_assets = api.list_assets(status='active')

def threeWhiteSoldiers(stock):
    try:
        stockData = getData(stock, 3)
        #if(stockData.open[1] < stockData.open[2] and stockData.open[2] < stockData.open[3] and stockData.high[1] < stockData.close[2] and stockData.high[2] < stockData.close[3]):
        if(stockData.open[0] < stockData.open[1] and stockData.open[1] < stockData.open[2]):
            return 1
        else:
            return 0
    except:
        return 0

def getData(stock, x):
    stockData = api.get_barset(stock, 'minute', limit=3).df
    stockData.columns = stockData.columns.to_flat_index()
    stockData.columns = [x[1] for x in stockData.columns]
    return stockData

def checkForPattern(stock):
    result = threeWhiteSoldiers(stock)
    if(result == 1):
        return 1
    else:
        return 0



def candleStickTrading():
    marketStatus = api.get_clock()
    x = 1
    while (marketStatus.is_open == False):
        for asset in active_assets:
            pattern = checkForPattern(asset.symbol)
            if(pattern != 0):
                if(pattern == 1):
                    patternPresent = "Three White Soldiers"
                print("Stock: " + asset.symbol + " Has pattern: " + patternPresent)
            time.sleep(.1)
            x = x + 1
            print(x)

=======
from yahoo_fin import options
import alpaca_trade_api as api
import time
import pandas as pd

apiPublicKey = 'PKAN2Q11ESBVLJB3AXY3'
apiPrivateKey = 'livscawL2BfWyVmp8oUF2NYkWEHsAdJQz0oRHrot'
alpacaEndPoint = 'https://paper-api.alpaca.markets'
stockDataFile = pd.read_csv('top500Stocks')

api = api.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')

active_assets = api.list_assets(status='active')

def threeWhiteSoldiers(stock):
    try:
        stockData = getData(stock, 3)
        #if(stockData.open[1] < stockData.open[2] and stockData.open[2] < stockData.open[3] and stockData.high[1] < stockData.close[2] and stockData.high[2] < stockData.close[3]):
        if(stockData.open[0] < stockData.open[1] and stockData.open[1] < stockData.open[2]):
            return 1
        else:
            return 0
    except:
        return 0

def getData(stock, x):
    stockData = api.get_barset(stock, 'minute', limit=3).df
    stockData.columns = stockData.columns.to_flat_index()
    stockData.columns = [x[1] for x in stockData.columns]
    return stockData

def checkForPattern(stock):
    result = threeWhiteSoldiers(stock)
    if(result == 1):
        return 1
    else:
        return 0



def candleStickTrading():
    marketStatus = api.get_clock()
    x = 1
    while (marketStatus.is_open == False):
        for asset in active_assets:
            pattern = checkForPattern(asset.symbol)
            if(pattern != 0):
                if(pattern == 1):
                    patternPresent = "Three White Soldiers"
                print("Stock: " + asset.symbol + " Has pattern: " + patternPresent)
            time.sleep(.1)
            x = x + 1
            print(x)

>>>>>>> 9ff58c1302e602741f0947bbad89b59bb49271da
candleStickTrading()
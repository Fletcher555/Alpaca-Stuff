import alpaca_trade_api as api
from datetime import datetime
from apiClass import info
import numpy as np
import apiClass
import pandas as pd

i = info()
apiPublicKey = i.apiPublic()
apiPrivateKey = i.apiPrivate()
alpacaEndPoint = i.apiLink()
stockDataFile = pd.read_csv(r'C:\Users\Milo\Documents\top500Stocks.csv')

api = api.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')


def getData(stock, x, stockDataCSV):
    stockData = api.get_barset(stock, 'day', limit=5).df
    stockData.columns = stockData.columns.to_flat_index()
    stockData.columns = [x[1] for x in stockData.columns]
    stockDataCSV.loc[x] = np.array([stock,
                                  stockData.open[0], stockData.high[0], stockData.low[0], stockData.close[0],
                                  stockData.open[1], stockData.high[1], stockData.low[1], stockData.close[1],
                                  stockData.open[2], stockData.high[2], stockData.low[2], stockData.close[2],
                                  stockData.open[3], stockData.high[3], stockData.low[3], stockData.close[3],
                                  stockData.open[4], stockData.high[4], stockData.low[4], stockData.close[4],])
    stockDataCSV.to_csv(r'C:\Users\Milo\Documents\data.csv')

def Hammer(x):
    stockData = pd.read_csv(r'C:\Users\Milo\Documents\data.csv')
    if(stockData.Close1[x] == stockData.High1[x] and (stockData.Open1[x] - stockData.Low1[x])/2 > (stockData.Close1[x] - stockData.Open1[x])):
        return True
    else:
        return False

def threeBlackCrows(x):
    stockData = pd.read_csv(r'C:\Users\Milo\Documents\data.csv')
    if(stockData.High2[x] < stockData.Open1[x] and stockData.High3[x] < stockData.Open2[x] and stockData.Low1[x] > stockData.Close2[x] and stockData.Low2[x] > stockData.Close3[x]):
        return True
    else:
        return False

def stopLossTakeProfitQTY(x):
    stockData = pd.read_csv(r'C:\Users\Milo\Documents\data.csv')
    stopLoss = (stockData.Close1[x])*0.98
    takeProfit = (stockData.Close1[x])*1.02
    accountInfo = api.get_account()
    QTY = round((float((accountInfo.cash)) * 0.2) / stockData.Close1[x])
    return QTY, takeProfit, stopLoss

def candleStickPatternChecker(x):
    if(Hammer(x) == True):
        return 1
    if(threeBlackCrows(x) == True):
        return 2
    else:
        return 0


def candleStickTrader():
    stockDataCSV = pd.DataFrame(columns=np.array(['Stock',
                                         'Open1', 'High1', 'Low1', 'Close1',
                                         'Open2', 'High2', 'Low2', 'Close2',
                                         'Open3', 'High3', 'Low3', 'Close3',
                                         'Open4', 'High4', 'Low4', 'Close4',
                                         'Open5', 'High5', 'Low5', 'Close5']))
    stockDataCSV.to_csv(r'C:\Users\Milo\Documents\data.csv')
    for x in range (199):
        getData(stockDataFile.Symbol[x], x, stockDataCSV)
        outcome = candleStickPatternChecker(x)
        print(stockDataFile.Symbol[x])
        if(outcome == 1):
            result = stopLossTakeProfitQTY(x)
            print("Hammer on: " + stockDataFile.Symbol[x] + " You should buy")
            #api.submit_order(symbol=stockDataFile.Symbol[x], qty=result[0], side='sell', type='market', time_in_force='day', stop_loss=dict(stop_price=result[2]), take_profit=dict(limit_price=result[1]))
        elif(outcome == 2):
            result = stopLossTakeProfitQTY(x)
            print("Three Black Crows on: " + stockDataFile.Symbol[x] + "You should buy")
            #api.submit_order(symbol=stockDataFile.Symbol[x], qty=result[0], side='buy', type='market', time_in_force='day', stop_loss=dict(stop_price=result[1]), take_profit=dict(limit_price=result[2]))


candleStickTrader()
print("done")
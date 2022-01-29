import datetime as dt
from apiClass import info
from alpaca_trade_api import TimeFrame, TimeFrameUnit
import alpaca_trade_api as api
import numpy as np
import pandas as pd

import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="stock_database"
)
mycursor = db.cursor()

i = info()
apiPublicKey = i.apiPublic()
apiPrivateKey = i.apiPrivate()

alpacaEndPoint = i.apiLink()

datePeriodStart = dt.date(2021, 1, 1)
datePeriodEnd = dt.date(2022, 1, 1)

daysBetweenPeriod = (datePeriodEnd - datePeriodStart).days
intraDayDataDensity = 'day'
stock = ['GME', 'TSLA', 'CCJ', 'SPY', 'AAPL', 'MSFT', 'FB', 'NVDA', 'GOOG', 'BB', 'AMC', 'PLTR', 'DASH', 'MMM', 'DIS', 'KO']

#print(alpacaEndPoint)
api = api.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')


def getHistoricalData():
    stockDataCSV = pd.DataFrame(columns=np.array(['Stock', 'Open', 'Close', 'High', 'Low', 'Volume']))
    stockDataCSV.to_csv(r'C:\Users\Milo\Documents\data.csv')
    counter = 0
    for x in range(daysBetweenPeriod):
        newDatePeriodStart = datePeriodStart + dt.timedelta(days=x)
        newDatePeriodEnd = datePeriodStart + dt.timedelta(days=(x+1))
        if(newDatePeriodEnd > datePeriodEnd):
            newDatePeriodStart = datePeriodStart + dt.timedelta(days=(x))
            newDatePeriodEnd = newDatePeriodEnd - dt.timedelta(days=(newDatePeriodEnd - datePeriodEnd).days)

        stockData = api.get_bars(stock, TimeFrame(5, TimeFrameUnit.Minute), start=newDatePeriodStart.isoformat(),
                                 end=newDatePeriodEnd.isoformat(), adjustment='raw').df
        #print(stockData.to_string())
        for index, row in stockData.iterrows():

            try:
                #print(index)
                sql = "INSERT INTO stockData (stockSymbol, periodTimeStamp, openPrice, closePrice, lowPrice, highPrice, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (stock, index, row.open*100, row.close*100, row.low*100, row.high*100, row.volume)
                mycursor.execute(sql, val)
                db.commit()
            except mysql.connector.errors.IntegrityError  as err:
                counter = counter + 1
                print(counter)





        #print("Start date: " + newDatePeriodStart.isoformat() + " End date: " + newDatePeriodEnd.isoformat())







getHistoricalData()
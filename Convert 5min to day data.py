import datetime as dt
from apiClass import info
import pandas as pd
import numpy as np


import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="stock_database"
)
mycursor = db.cursor(buffered=True)

stock = 'AAPL'
i = info()
apiPublicKey = i.apiPublic()
apiPrivateKey = i.apiPrivate()
alpacaEndPoint = i.apiLink()



def buySellSQLDatabase():
    mycursor.execute("USE Stock_DataBase;")
    mycursor.execute("SELECT MIN(periodTimeStamp) FROM stockdata;")
    firstDate = mycursor.fetchone()
    firstDate = firstDate[0]

    mycursor.execute("SELECT MAX(periodTimeStamp) FROM stockdata;")
    endDate = mycursor.fetchone()
    endDate = endDate[0]
    currentDateTime = firstDate
    x = 0
    stockDataCSV = pd.DataFrame(columns=np.array(['stockSymbol', 'periodTimeStamp', 'openPrice', 'closePrice', 'lowPrice', 'highPrice', 'volume']))
    stockDataCSV.to_csv(r'C:\Users\Milo\Documents\PythonPandasFiles\dayDataTempFile.csv')

    yearLongCSV = pd.DataFrame(columns=np.array(['Date', 'Open', 'High', 'Low', 'Close']))
    yearLongCSV.to_csv(r'C:\Users\Milo\Documents\PythonPandasFiles\yearLongDataFile.csv')
    y = 0
    while(currentDateTime < endDate):

        currentDateTime = currentDateTime + dt.timedelta(minutes=(5))

        if(currentDateTime.date() == (currentDateTime - dt.timedelta(minutes=5)).date()):
            mycursor.execute("USE Stock_DataBase;")
            sqlQuery = "SELECT * FROM stockdata WHERE periodTimeStamp = %s AND stockSymbol = %s;"
            val = (currentDateTime, stock)
            mycursor.execute(sqlQuery, val)
            result = mycursor.fetchone()
            if(result != None):
                stockDataCSV.loc[x] = np.array([result[1], result[2], result[3], result[4], result[5], result[6], result[7]])
                stockDataCSV.to_csv(r'C:\Users\Milo\Documents\PythonPandasFiles\dayDataTempFile.csv')
            x = x + 1
        else:
            if (result != None):
                mycursor.execute("USE yearLongFile;")
                sql = "INSERT INTO stockData (stockSymbol, periodTimeStamp, openPrice, closePrice, lowPrice, highPrice, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                stockDayData = pd.read_csv(r'C:\Users\Milo\Documents\PythonPandasFiles\dayDataTempFile.csv')
                print(stockDayData.to_string())
                openPrice = stockDayData.openPrice[0]
                closePrice = stockDayData.closePrice.iloc[-1]
                lowPrice = stockDayData.lowPrice.min()
                highPrice = stockDayData.highPrice.max()
                volume = stockDayData.volume.sum()
                val = (stock, (currentDateTime - dt.timedelta(minutes=5)).date(), openPrice.item(), closePrice.item(), lowPrice.item(), highPrice.item(), volume.item())
                mycursor.execute(sql, val)
                db.commit()

                yearLongCSV.loc[y] = np.array([(currentDateTime - dt.timedelta(minutes=5)).date(), openPrice.item()/100, highPrice.item()/100, lowPrice.item()/100, closePrice.item()/100])
                yearLongCSV.to_csv(r'C:\Users\Milo\Documents\PythonPandasFiles\yearLongDataFile.csv')
            y = y + 1

            x = 0
            filename = r'C:\Users\Milo\Documents\PythonPandasFiles\dayDataTempFile.csv'
            f = open(filename, "w+")
            f.close()
            stockDataCSV = pd.DataFrame(columns=np.array(['stockSymbol', 'periodTimeStamp', 'openPrice', 'closePrice', 'lowPrice', 'highPrice', 'volume']))
            stockDataCSV.to_csv(r'C:\Users\Milo\Documents\PythonPandasFiles\dayDataTempFile.csv')

buySellSQLDatabase()



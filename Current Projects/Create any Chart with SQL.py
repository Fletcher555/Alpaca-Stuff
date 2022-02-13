from validInputs import TestInputs
from datetime import datetime
import datetime as dt
from apiClass import info
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="stock_database"
)
myCursor = db.cursor(buffered=True)

i = info()
apiPublicKey = i.apiPublic()
apiPrivateKey = i.apiPrivate()
alpacaEndPoint = i.apiLink()


def takeInputs(inputRequest, inputArray):
    stockTypeTrue = False
    stockRequest = None
    while not stockTypeTrue:
        stockRequest = input(inputRequest)
        testInputs = TestInputs()
        stockTypeTrue = testInputs.tester(stockRequest, inputArray)
        if stockRequest == '1':
            # Special charecter that spits back a list of accepted answers
            print(inputArray)
            stockTypeTrue = False
    return stockRequest


def takeCustomDataDensity():
    done = False
    dataDensity = None
    while not done:
        dataDensity = input(
            "What would you like the custom data density to be? '1' View Options, or input accepted values: ")
        try:
            int(dataDensity)

            while int(dataDensity) % 5 != 0 or int(dataDensity) / 5 > 60:
                if dataDensity == '1':
                    print("Please enter any integer that is divisible by 5 that is less than 300.")
                dataDensity = input(
                    "What would you like the custom data density to be? '1' View Options, or input accepted values: ")
                try:
                    int(dataDensity)
                except ValueError:
                    dataDensity = 4
            done = True
        except ValueError:
            print("Enter a valid input please")
    return dataDensity


def takeStartDate(minDate, maxDate):
    err = True
    startDateObj = None
    while err:
        startDate = input(
            "What would you like the start datetime to be? '1' View Options, format is 'YY/MM/DD HH:MM:SS' or '2' for Min Date: ")

        if startDate == '1':
            print("The Min datetime that can be inputed is: " + str(minDate) +
                  " Any datetime entered before this will automatically update to the min datetime. Also please note any Date entered after: " +
                  str(maxDate - dt.timedelta(minutes=5)) + " Will be invalid.")

        elif startDate == '2':
            startDateObj = minDate
            err = False
        else:
            try:
                startDateObj = datetime.strptime(startDate, '%y/%m/%d %H:%M:%S')  # 21/06/06 9:30:00
                if startDateObj <= minDate:
                    startDateObj = minDate

                if startDateObj < maxDate:
                    err = False
                else:
                    print("Date is above Max date please try again.")
            except ValueError:
                print("Invalid datetime please try again.")

    return startDateObj

def stockSymbol():
    stock = takeInputs(
        "Which stock would you like to generate a candlestick chart for? '1' View Options, or input accepted values: ",
        TestInputs.createAnyChartWithSQLStock)
    return stock

def dataDensity():
    dataDensity = takeInputs(
        "What would you like the data Density of your candlestick chart to be? '1' View Options, or input accepted values: ",
        TestInputs.createAnyChartWithSQLDataDensity)

    if dataDensity == 'Custom':
        dataDensity = takeCustomDataDensity()

    return dataDensity

def fetchMinMaxDate(stock):
    myCursor.execute("USE Stock_DataBase;")
    query = "SELECT MIN(periodTimeStamp) FROM stockdata WHERE stockSymbol = '%s';"
    myCursor.execute(query % stock)
    minDate = myCursor.fetchone()

    myCursor.execute("USE Stock_DataBase;")
    query = "SELECT MAX(periodTimeStamp) FROM stockdata WHERE stockSymbol = '%s';"
    myCursor.execute(query % stock)
    maxDate = myCursor.fetchone()

    return minDate[0], maxDate[0]

def run():
    stock = stockSymbol()
    density = dataDensity()
    minMaxDate= fetchMinMaxDate(stock)
    minDate = minMaxDate[0]
    maxDate = minMaxDate[1]
    startDate = takeStartDate(minDate, maxDate)

    print(stock + density + str(startDate))


run()

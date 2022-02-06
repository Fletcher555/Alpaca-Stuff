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


def takeStartDate(stock):
    err = True
    while err:
        startDate = input(
            "What would you like the start datetime to be? '1' View Options, format is 'YY/MM/DD HH:MM:SS': or '2' for Min Date")
        myCursor.execute("USE Stock_DataBase;")
        query = "SELECT MIN(periodTimeStamp) FROM stockdata WHERE stockSymbol = '%s';"
        myCursor.execute(query % stock)
        minDate = myCursor.fetchone()

        myCursor.execute("USE Stock_DataBase;")
        query = "SELECT MAX(periodTimeStamp) FROM stockdata WHERE stockSymbol = '%s';"
        myCursor.execute(query % stock)
        maxDate = myCursor.fetchone()

        if startDate == '1':
            print("The Min datetime that can be inputed is: " + str(minDate[
            0]) + " Any datetime entered before this will automatically update to the min datetime. Also please note any Date entered after: " + str(
                maxDate[0] - dt.timedelta(minutes=(5))) + " Will be invalid.")
        else:
            try:
                startDateObj = datetime.strptime(startDate, '%y/%m/%d %H:%M:%S')  # 21/06/06 9:30:00
                if startDateObj <= minDate[0]:
                    startDateObj = minDate[0]

                if startDateObj < maxDate[0]:
                    err = False
                else:
                    print("Date is above Max date please try again.")
            except ValueError:
                print("Invalid datetime please try again.")

    return startDateObj, minDate[0], maxDate[0]

# def takeEndDate(stock, startDate):
#     err = True
#     while err:
#         endDate = input(
#             "What would you like the end datetime to be? '1' View Options, format is 'YY/MM/DD HH:MM:SS': ")
#         myCursor.execute("USE Stock_DataBase;")
#         query = "SELECT MAX(periodTimeStamp) FROM stockdata WHERE stockSymbol = '%s';"
#         myCursor.execute(query % stock)
#         maxDate = myCursor.fetchone()
#         if endDate == '1':
#             print("The Max date that can be inputed is: " + str(maxDate[0]) + "Any date that is inputed after this date will automatically be formated to this date")


def run():
    stock = takeInputs(
        "Which stock would you like to generate a candlestick chart for? '1' View Options, or input accepted values: ",
        TestInputs.createAnyChartWithSQLStock)

    dataDensity = takeInputs(
        "What would you like the data Density of your candlestick chart to be? '1' View Options, or input accepted values: ",
        TestInputs.createAnyChartWithSQLDataDensity)

    if dataDensity == 'Custom':
        dataDensity = takeCustomDataDensity()

    startDate = takeStartDate(stock)
    print(startDate)

    # endDate = takeEndDate(stock, startDate)


run()



from apiClass import info

import alpaca_trade_api as api


i = info()
apiPublicKey = i.apiPublic()
apiPrivateKey = i.apiPrivate()
alpacaEndPoint = i.apiLink()

api = api.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')


def cancelOrders():
    orders = api.list_orders(status="open")
    for order in orders:
        api.cancel_order(order.id)

def makeOrder():
    stock = input("What stock would you like?")
    type = input("'sell' or 'buy'?")
    qty = int(input("How Many Shares would you like?"))
    orderType = input("Limit or Market order?")
    if(orderType == "Limit"):
        limitPrice = float(input("Enter limit price"))
        api.submit_order(symbol=stock, qty=qty, side=type, type= 'limit', time_in_force='day', limit_price=limitPrice)
        return 1
    elif(orderType == "Market"):
        api.submit_order(symbol = stock, qty=qty, side = type, type = 'market', time_in_force = 'day')
        return 1
    else:
        return 0

def closeAllPositions():
    api.close_all_positions()

def listPositions():
    portfolio = api.list_positions()
    for position in portfolio:
        print("{} shares of {}".format(position.qty, position.symbol))


def run():
    request = input("What would you like to do: Cancel Orders '1', Make Order '2', Close All Positions '3', List Current Holdings '4'")
    if(request == "1"):
        cancelOrders()
    if(request == "2"):
        x = makeOrder()
        while(x != 1):
            x = makeOrder()
    if(request == "3"):
        closeAllPositions()
    if(request == "4"):
        listPositions()

run()

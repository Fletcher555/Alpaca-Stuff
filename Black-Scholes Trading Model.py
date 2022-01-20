from yahoo_fin import options
import alpaca_trade_api as api



apiPublicKey = 'PKFO1HKRRFY8ADDND4WG'
apiPrivateKey = 'AwihaCN5bOr7H5iP6T5kpbjPZxHADDKbHQxPQjI4'
#stock = input("What stock are you interested in?")
stock = 'CCJ'
alpacaEndPoint = 'https://paper-api.alpaca.markets'
api = api.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')

def theModel():
    stock = getInputs(2)
    assetPrice = api.get_barset(stock, 'minute', limit = 1).df
    assetPrice.columns = assetPrice.columns.to_flat_index()
    assetPrice.columns = [x[1] for x in assetPrice.columns]
    assetPrice.reset_index(inplace=True)
    assetPrice = assetPrice.open[0]


    currentInput = getInputs(1)
    if(currentInput == 1):
        expirationDate = getInputs(2)
        if(expirationDate == 1):
            expirationDate = "Jan 18"


def getInputs(x):
    if(x == 1):
        typeOfOption = int(input("Would you like to get info about the Call '1' or Put '2' Option?"))
        return typeOfOption
    if(x == 2):
        expirationDate = int(input("What expiration date are you interested in?: " + options.get_expiration_dates(stock)[0] + " '1' " + options.get_expiration_dates(stock)[1] + " '2' " + options.get_expiration_dates(stock)[2] + " '3' "))
        return expirationDate


theModel()
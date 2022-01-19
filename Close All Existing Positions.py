import alpaca_trade_api as tradeapi
import time

apiPublicKey = 'PKFO1HKRRFY8ADDND4WG'
apiPrivateKey = 'AwihaCN5bOr7H5iP6T5kpbjPZxHADDKbHQxPQjI4'
alpacaEndPoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(apiPublicKey, apiPrivateKey, alpacaEndPoint, api_version='v2')

def closeAllPositions():
    api.get_account


closeAllPositions()
import alpaca_trade_api as tradeapi

class Alpaca(object):
    def __init__(self):
        self.key = 'PKQFCYN1MCXGCSRDCKYH'
        self.secret = 'RJR8rq4Wo6pP5EzM3ABURAFX1C7TYPucnFjsq5pR'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)


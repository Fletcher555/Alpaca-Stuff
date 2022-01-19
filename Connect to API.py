import alpaca_trade_api as tradeapi

class Alpaca(object):
    def __init__(self):
        self.key = 'PK2VQWH7X8DAC2LRTZIN'
        self.secret = 'pGe1Wx0t8K4rZXbFelRMDm8sMHTQdtNvWtNCQqHw'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)



print("hello")
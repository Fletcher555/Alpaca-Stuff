import alpaca_trade_api as tradeapi
import time

class Alpaca(object):
    def __init__(self):
        self.key = 'PKQFCYN1MCXGCSRDCKYH'
        self.secret = 'RJR8rq4Wo6pP5EzM3ABURAFX1C7TYPucnFjsq5pR'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)
        self.symbol = 'SPY'
        self.current_order = None # when variable is not "none", we have open order
        self.last_price = 100

        # this bot is only limited to one position btw (short or long)

        try:
            self.position = int(self.api_get_position(self.symbol).qty)
        except:
            self.position = 0

    #This is the algorythm

    def submit_order(self, target):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)   #if current order is open, it will cancel the second

        delta = target - self.position
        if delta == 0:
            return
        print(f'Processing order for {target} shares')

        if delta > 0:
            buy_quantity = delta
            if self.position < 0:
                buy_quantity = min(abs(self.position), buy_quantity)
            print(f'Buying {buy_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol,buy_quantity, 'buy', 'limit', 'day', self.last_price)

        elif delta < 0:
            sell_quantity = abs(delta)
            if self.position > 0:
                sell_quantity = min(abs(self.position), sell_quantity)

            print(f'Selling {sell_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol,sell_quantity,'sell','limit','day',self.last_price)

while __name__== '__main__':
    trades = Alpaca()
    trades.submit_order(3)
    time.sleep(8)






<<<<<<< HEAD
=======


>>>>>>> 9ff58c1302e602741f0947bbad89b59bb49271da

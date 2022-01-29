def sumbit_order(self, target):
    if self.current_order is not None:
        self.api.cancel_order(self.current_order.id)

    delta = target - self.position
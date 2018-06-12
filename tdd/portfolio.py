class Portfolio(object):

    def __init__(self):
        self.stocks = []

    def buy(self, name, shares, price):
        self.stocks.append([name, shares, price])
        if not isinstance(shares, int):
            raise Exception("shares must be an integer")

    def cost(self):
        amt = 0.0
        for name, shares, price in self.stocks:
            amt += shares * price
        return amt

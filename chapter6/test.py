#外观类
class Fund(object):

    def __init__(self):
        self.stocka = StockA()
        self.stockb = StockB()
        self.realty = Realty()

    def buy(self):
        self.stocka.buy()
        self.stockb.buy()
        self.realty.buy()

    def sell(self):
        self.stocka.sell()
        self.stockb.sell()
        self.realty.sell()

#投资股票A类
class StockA(object):

    def buy(self):
        print('buy StockA')

    def sell(self):
        print('sell StockA')

#投资股票B类
class StockB(object):

    def buy(self):
        print('buy StockB')

    def sell(self):
        print('sell StockB')

#投资房地产
class Realty(object):
    def buy(self):
        print('buy Reaty')

    def sell(self):
        print('sell Realty')

if __name__=='__main__':
    fund = Fund()
    fund.buy()
    fund.sell()

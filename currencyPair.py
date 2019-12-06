class CurrencyPair():
    baseCurrency = ''
    quoteCurrency = ''

    def __init__(self, pair):
        # print("[CurrencyPair.__init__]")
        # print(f"class for {pair} created")
        currencies = pair.split('/')
        self.buy = []
        self.sell = []
        self.baseCurrency = currencies[0].strip()
        self.quoteCurrency = currencies[1].strip()

    def displayPair(self):
        print("[CurrencyPair.displayPair]")
        print(self.baseCurrency)
        print(self.quoteCurrency)

    def displaySell(self):
        print(self.sell)

    def displayBuy(self):
        print(self.buy)
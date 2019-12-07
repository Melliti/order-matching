import currencyPair

class PairsList(object):
    __pairs = {}
    __instance = None
    __register = []
    
    @staticmethod
    def getInstance():
        if PairsList.__instance == None:
            PairsList()
        return PairsList.__instance 

    def __init__(self):
        if PairsList.__instance != None:
            raise Exception("PairsList is a Singleton. us PairsList.getInstance")
        else:
            PairsList.__instance = self

    def findMatchingBuyOrder(self, order):
        instance = self.__pairs[order[2]]
        buyOrders = instance.buy
        for buyOrder in buyOrders:
            if (len(buyOrder) < 6):
                if (buyOrder[4] > order[4]):
                    print(order[0] + " match to " + buyOrder[0])
                    order.append(buyOrder[0])
                    self.__register.append(order)
                    buyOrders.remove(buyOrder)
                    return True
        self.__register.append(order)
        return False

    def findMatchingSellOrder(self, order):
        instance = self.__pairs[order[2]]
        sellOrders = instance.sell
        for sellOrder in sellOrders:
            if (len(sellOrder) < 6):
                if (sellOrder[4] < order[4]):
                    print(order[0] + " match to " + sellOrder[0])
                    order.append(sellOrder[0])
                    self.__register.append(order)
                    sellOrders.remove(sellOrder)
                    return True
        self.__register.append(order)
        return False

    def addPairToDict(self, pairs):
        if not pairs in self.__pairs:
            self.__pairs[pairs] = currencyPair.CurrencyPair(pairs)
    
    def addOrderToPair(self, order):
        instance = self.__pairs[order[2]]
        if order[3] == " SELL":
            match = self.findMatchingBuyOrder(order)
        else:
            match = self.findMatchingSellOrder(order)
        # print(order)
        # print(match)
        if (match == False):
            instance.sell.append(order) if order[3] == " SELL" else instance.buy.append(order)
        self.__register.append(order)
        

    def showPairs(self):
        print("[PairsList.showPairs]")
        for key, value in self.__pairs.items():
            print(key)
            print(value)

    def displayAll(self, row):
        instance = self.__pairs[row]
        print(f"for {row}")
        # for key, value in self.__pairs.items():
            # print(key)
            # print(value.displayBuy())
        # print(instance)
        instance.displayBuy()
        instance.displaySell()
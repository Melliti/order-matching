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

    def addPairToDict(self, pairs):
        if not pairs in self.__pairs:
            self.__pairs[pairs] = currencyPair.CurrencyPair(pairs)
    
    def addOrderToPair(self, order):
        self.__register.append(order)
        instance = self.__pairs[order[2]]
        instance.sell.append(order) if order[3] == " SELL" else instance.buy.append(order)
        # instance.displayBuy()


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
        print(self.__register)
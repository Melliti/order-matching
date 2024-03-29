import sys
import csv
import pairsList

class csvReader:
    pairs = pairsList.PairsList.getInstance()

    def readCSV(self):
        with open(sys.argv[1], 'r') as csvFile:
            datas = csv.reader(csvFile, delimiter=",")
            count = 0
            for row in datas:
                if count == 0:
                    count += 1
                    continue
                self.pairs.addPairToDict(row[2])
                self.pairs.addOrderToPair(row)
        self.pairs.completeRegister()

    def writeCSV(self):
        register = self.pairs.getRegister()
        file = open("myMatch.csv", "w")
        file.write("id,account,pair,action,price,match\n")
        for order in register:
            orderStr = ","
            orderStr = orderStr.join(order)
            file.write(orderStr + "\n")

mycsv = csvReader()
mycsv.readCSV()
mycsv.writeCSV()
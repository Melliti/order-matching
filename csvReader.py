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
                # print(row)
                # self.pairs.displayAll(row)
            # print(self.pairs.showPairs())
            # self.pairs.showPairs()
        self.pairs.displayAll(' EUR/USD')
        self.pairs.displayAll(' CAD/USD')




mycsv = csvReader()
mycsv.readCSV()
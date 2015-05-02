__author__ = 'zephyros'
import math

class TfIdf:
    def __init__(self, dicts):
        self.dicts = dicts

    def getCount(self):
        count = {}
        for i in range(len(self.dicts)):
            dict =self.dicts[i]
            for d in dict:
                if not d in count:
                    count[d] = [i]
                else:
                    if not i in count[d]:
                        count[d].append(i)
        return count

    def getScore(self):
        count = self.getCount()
        score = {}
        for word in count:
            wholeNumber = 0
            for dict in self.dicts:
                if word in dict:
                    wholeNumber += dict[word]

            score[word] = math.log(1 + wholeNumber, 2) * len(count[word])
        return score
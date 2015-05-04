__author__ = 'zephyros'
import math

class ScoreWords:
    def __init__(self, dicts, ne):
        self.dicts = dicts
        self.nameEntity = ne

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

    def isNameEntity(self, word):
        for d in self.nameEntity:
            if word in self.nameEntity[d]:
                if d == 'O':
                    return False
                else:
                    return True
        return False

    def getScore(self):
        count = self.getCount()
        score = {}
        for word in count:
            wholeNumber = 0
            for dict in self.dicts:
                if word in dict:
                    wholeNumber += dict[word]

            k = 2 if self.isNameEntity(word) else 1
            score[word] = math.log(1 + wholeNumber, 2) * len(count[word]) * k

        return score
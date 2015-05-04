__author__ = 'zephyrYin'
import sys
from random import randint
import

class Article:
    def __init__(self, path):
        self.path = path
        self.content = []
        self.extraction = []

    def loadArticle(self):
        file = open(self.path)
        lines = file.readlines()
        file.close()
        status = 0
        tmp = []
        for line in lines:
            if line == '\n':
                best = self.pickBest(tmp)
                index = randint(0,len(best)-1)
                self.extraction.append(best[index])
                status = 0
                tmp = []
                continue
            elif status == 0:
                self.content.append(line.strip('\n'))
                status += 1
            else:
                tmp.append(line.strip('\n'))

    def pickBest(self, candidates):
        max = 0
        best = []
        for c in candidates:
            credit, content = self.transform(c)
            if credit > max:
                max = credit
                best = []
                best.append(content)
            elif credit == max:
                best.append(content)
        return best


    def transform(self, line):
        credit = float(line[0:4])
        content = line[5:]
        left = content.index('(')
        right = content.index(')')
        return credit, content[left+1:right]

if __name__ == "__main__":

    file = "d04aOpenieResult/1.txt"

    a = Article(file)
    a.loadArticle()
    print(len(a.content))
    print(len(a.extraction))
    for e in a.extraction:
        print(e)
        print('......')

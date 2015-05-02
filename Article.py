__author__ = 'zephyros'
from random import randint
import nltk.tokenize
from UseLess import Useless


class Article:
    def __init__(self, path):
        self.path = path
        self.content = []
        self.extraction = []
        self.extractionWords = []
        self.useless = [',', ';', ':', '(', ')','[',']']
        self.wordFrequency = {}
        self.loadArticle()

    def loadArticle(self):
        file = open(self.path)
        lines = file.readlines()
        file.close()
        status = 0
        tmp = []
        for line in lines:
            if line == '\n':
                if len(tmp) == 0:
                    self.content.pop()
                    status = 0
                    continue
                best = self.pickBest(tmp)
                index = randint(0,len(best)-1)
                self.extraction.append(best[index])
                words = self.sen2Words(best[index])
                self.extractionWords.append(words)
                status = 0
                tmp = []
                continue
            elif status == 0:
                self.content.append(line.strip('\n'))
                status += 1
            else:
                tmp.append(line.strip('\n'))
        self.wordFrequency = self.gatherWords(self.extractionWords)

    def sen2Words(self, sent):
        u = Useless('prep_list')
        words = nltk.tokenize.word_tokenize(sent)
        result = []
        for w in words:
            if len(w) >= 2 and not w in u.words:
                result.append(w.lower())
        return result

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

    def gatherWords(self, wordList):
        wordFrequency = {}
        for words in wordList:
            for word in words:
                if word in wordFrequency:
                    wordFrequency[word] += 1
                else:
                    wordFrequency[word] = 1
        return wordFrequency

    def commonWords(self, article):
        words = {}
        for wordA in self.wordFrequency:
            for wordB in article.wordFrequency:
                if wordA == wordB:
                    if wordA in words:
                        words[wordA] += 1
                    else:
                        words[wordA] = 1
        return words


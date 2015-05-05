__author__ = 'zephyros'

import math
from Pagerank import PageRank
from Article import Article
from NameEntity import NE
from ScoreWords import ScoreWords
import nltk
import os

class TextRank:
    def __init__(self, articlePaths, nerPath):
        self.pathList = articlePaths
        self.nerPathList = nerPath
        self.wordScore = self.getWordScore()

    def summary(self, limit):
        indexAndScore, sentences = self.getSentenceRank()
        s = ''
        cnt = 0
        lineCnt = 0
        while cnt < 200:
            line = sentences[indexAndScore[lineCnt][0]]
            s += line + ' '
            lineCnt += 1
            cnt += len(nltk.tokenize.word_tokenize(line))
        return s

    def getSentenceRank(self):
        self.articles = [Article(f) for f in self.pathList]
        lines = []
        lineWords = []
        for article in self.articles:
            zipped = zip(article.content, article.extractionWords)
            for z in zipped:
                lines.append(z[0])
                lineWords.append(z[1])
        nodes = [i for i in range(len(lines))]
        graph = self.constructGraph(nodes, lineWords)
        pR = PageRank(graph, 0.85, 100)
        nodeScores = pR.rank()
        dict = {}
        for i in range(len(nodeScores)):
            dict[i] = nodeScores[i]
        sentenceRank = sorted(dict.items(), key=lambda d : d[1], reverse=True)
        return sentenceRank, lines

    def constructGraph(self, nodes, wordsList):
        print('construct graph...')
        graph = []
        for node in nodes:
            row = []
            for neiNoe in nodes:
                if node == neiNoe:
                    row.append(0)
                else:
                    row.append(self.similarity(wordsList[node], wordsList[neiNoe]))
            graph.append(row)
        print(graph)
        print('graph construdted')
        return graph

    def loopDir(self, rootDir):
        d = []
        for lists in os.listdir(rootDir):
            path = os.path.join(rootDir, lists)
            d.append(path)
        return d

    def getWordScore(self):
        articles = [Article(f) for f in self.pathList]
        articleWords = [article.wordFrequency for article in articles]

        ne = NE(self.loopDir(self.nerPathList))
        t = ScoreWords(articleWords, ne.dict)
        scores = t.getScore()
        return scores

    def similarity(self, wordsA, wordsB):
        cnt = 0
        for word in wordsA:
            if word in wordsB:
                cnt += (1 + math.log(self.wordScore[word],2))
        result = cnt / (math.log(len(wordsA)) + math.log(len(wordsB)))
        return result

if __name__ == "__main__":

    fileNames = ['d04aOpenieResult/' + str(i+1) + '.txt' for i in range(7)]
    tR = TextRank(fileNames, 'ner/d04a')
    s = tR.summary(200)
    file = open('testRankSummary.txt', 'w')
    file.write(s)
    file.close()
    # dict = tR.getWordScore()
    # for d in dict:
    #     print(d, dict[d])
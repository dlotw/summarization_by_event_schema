__author__ = 'zephyros'

import math
from Pagerank import PageRank
from Article import Article
from NameEntity import NE
from ScoreWords import ScoreWords
import nltk
import DIR

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
        for g in graph:
            print(g)
        print('graph constructed')
        return graph

    def getWordScore(self):
        articles = [Article(f) for f in self.pathList]
        articleWords = [article.wordFrequency for article in articles]

        ne = NE(self.nerPathList)
        t = ScoreWords(articleWords, ne.dict)
        scores = t.getScore()

        return scores

    def similarity(self, wordsA, wordsB):
        cnt = 0
        for word in wordsA:
            if word in wordsB:
                if not word in self.wordScore:
                    cnt += 1
                else:
                    cnt += (1 + math.log(self.wordScore[word], 2))
        result = cnt / (1 + math.log(len(wordsA)) + math.log(len(wordsB)))
        return result




if __name__ == "__main__":
    nerDir = DIR.loopShallowDir('ner')
    DIR.mkdir('openieSummary')
    #l = ['d04a', 'd05a', 'd08b','d11b', 'd12b', 'd14c', 'd19d','d13c','d15c']
    for nD in nerDir:
        tmp = nD.split('/')
        # if tmp[1] in l:
        #     continue
       # print(tmp[0], tmp[1])
        #print(DIR.loopDeepDir(nD))
        docPath = DIR.loopShallowDir('openieOutput/' + tmp[1])
        tR = TextRank(docPath, DIR.loopDeepDir(nD))
        s = tR.summary(200)
        file = open( 'openieSummary/' + tmp[1] + '.txt', 'w')
        file.write(s)
        file.close()
        # dict = tR.getWordScore()
        # for d in dict:
        #     print(d, dict[d])
    # fileNames = ['d04aOpenieResult/' + str(i+1) + '.txt' for i in range(7)]
    # tR = TextRank(fileNames, 'ner/d04a')
    # s = tR.summary(200)
    # file = open('testRankSummary.txt', 'w')
    # file.write(s)
    # file.close()
    # dict = tR.getWordScore()
    # for d in dict:
    #     print(d, dict[d])